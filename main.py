import os
from flask import Flask, request, render_template_string
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'file_db',
    'host': 'mongodb://127.0.0.1:27017/'
}
db = MongoEngine()
db.init_app(app)

class File(db.Document):
    filename = db.StringField(required=True, max_length=100)
    file_type = db.StringField(max_length=50)
    file_size = db.IntField()
    data = db.FileField()
    metadata = db.DictField()  # Add metadata field

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            filename = file.filename
            file_type = os.path.splitext(filename)[1]
            file_size = len(file.read())  # Get file size
            file.seek(0)  # Reset file cursor
            uploaded_file = File(filename=filename, file_type=file_type, file_size=file_size, data=file)
            uploaded_file.save()
    uploaded_files = File.objects()
    return render_template_string('''
        <h1>File Upload</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Upload File</button>
        </form>
        {% if uploaded_files %}
        <h2>Uploaded Files:</h2>
        <ul>
            {% for file in uploaded_files %}
            <li>
                <strong>{{ file.filename }}</strong> - Type: {{ file.file_type }}, Size: {{ file.file_size }} bytes
            </li>
            {% endfor %}
        </ul>
        {% endif %}
    ''', uploaded_files=uploaded_files)

if __name__ == '__main__':
    app.run(debug=True)
