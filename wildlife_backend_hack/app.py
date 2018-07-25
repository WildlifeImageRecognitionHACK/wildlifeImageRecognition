"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, jsonify, render_template
app = Flask(__name__, static_url_path='')
#"C:\\repo\\wlir_web_ui\\wlir_web_ui\\dist"
from pymongo import MongoClient
import json
import pprint

client = MongoClient()
db = client['wirDB']

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
    table = db['userLabels2']
    result = db.list_collection_names()
    
    return jsonify({'results': tasks})

@app.route('/api')
def return_api():
    imageTable = db['organizations']
    result = imageTable.find()
    s = "{"
    for res in result:
        s += str(res) + ","
    s = s[:-1]
    s = s.replace("'", '"')
    s += "}"
    print(s)
    #json_res = json.loads(s)
    #pprint(json_res)
    #images = {}
    #for i in range(result.count())
     #   images[i] =
    return jsonify(s)


@app.route('/')
def welcome():
    return app.send_static_file('index.html')

    

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    app.run('0.0.0.0', PORT)
