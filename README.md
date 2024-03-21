# FlaskMongo
Connect a flask app to mongodb and upload files to the backend, and view their metadata.

Install MongoDB Community Server, and have an IDE of your choice (we used PyCharm), and optionally Postman API.

------------------------------------------------
The code relies on the following dependencies:
Flask
Flask-MongoEngine
MongoEngine

These can be installed via the in-built terminal on an IDE.
pip install Flask
pip install Flask-MongoEngine
pip install mongoengine
------------------------------------------------

Open up MongoDB Compass and create a new connection:

![image](https://github.com/AlphaNewt7/FlaskMongo/assets/71941891/e89955d3-19bb-4ab2-81d0-c551699c849a)

Connect to it, and create a database called file_db and a collection called file, this is where the files be uploaded.

Head back to your IDE, and then run the code, the instance will be created on port 5000 by default on your local machine, open it up on your browser.
Browse to a file and click on upload, it should return the metadata of the file and it should reflect on MongoDB.
