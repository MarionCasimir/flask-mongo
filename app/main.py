from flask import Flask
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://root:root@localhost:4000/test_db?authSource=admin"
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

#this will run when we do localhost:5000 >> will display Hello World

@app.route('/marion')
def hello_marion():
    return 'Hello, Marion!'
#this will run when we do localhost:5000/marion >> will display Hello Marion

@app.route('/stores')
def get_stores():
    result = mongo.db.stores.find() #stores information from the stores dd into the result variable
    result_str = json.dumps(list(result)) #converts result to list > jason.dumps converts list to a jason formatted string
    return '"stores": {}'.format(result_str)

@app.route('/stores/id/<int:id>') #this is forcing to enter an int for the id value
def get_stores_by_id(id):
    result = mongo.db.stores.find({"_id": id})
    result_str = json.dumps(list(result))
    return '"stores": {}'.format(result_str)

# check documentation - https://flask-pymongo.readthedocs.io/en/latest/

@app.route('/users')
def get_users():
    result = mongo.db.users.find() #stores information from the users dd into the result variable
    result_str = json.dumps(list(result)) #converts result to list > json.dumps converts to a json formatted string
    return '"users": {}'.format(result_str)


if __name__ == '__main__':
    app.run()

#http://flask.pocoo.org/docs/1.0/quickstart/
#https://flask-pymongo.readthedocs.io/en/latest/