"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, jsonify, render_template
app = Flask(__name__)
#"C:\\repo\\wlir_web_ui\\wlir_web_ui\\dist"
from pymongo import MongoClient
import pprint


def connect_database():
    client = MongoClient()
    db = client['wirDB']
    table = db['userLabels']
    result = table.find()
    return result


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/wir/api/get', methods=['GET'])
def get_tasks():
    client = MongoClient()
    db = client['wirDB']
    table = db['userLabels2']
    result = table.find()
    return jsonify({'results': tasks})

@app.route('/api')
def return_api():
    return jsonify({'result': tasks})



@app.route('/')
def welcome():
    return render_template('index.html')

    

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    connect_database()
    print("blabla")
    print("root folder web: ", app.instance_path)
    app.run(HOST, PORT)
