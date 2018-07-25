"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, jsonify, send_from_directory, url_for
app = Flask(__name__, static_url_path='')
from pymongo import MongoClient
import json

client = MongoClient()
db = client['wirDB']
images = {}



# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


def get_data_imagedb():
    image_table = db['image']
    image_data = image_table.find()
    i = 0
    for image in image_data:
        images[i] = image
        i += 1


@app.route('/api')
def return_image():
    imageTable = db['organizations']
    result = imageTable.find()
    s = "{"
    for res in result:
        print(type(res))
        s += str(res) + ","
    s = s[:-1]
    s = s.replace("'", '"')
    s += "}"
    return jsonify(s)


@app.route('/')
def welcome():
    return app.send_static_file('index.html')


@app.route('/images/')
def get_all_images():
    response = app.response_class(response=json.dumps(images),
                                  status=200,
                                  mimetype="application/json")
    return response
    # filename = "1039210COR1 031.jpg"
    # MEDIA_FOLDER = "C:\\Images\\results\\Animals"
    # imageLink = send_from_directory(MEDIA_FOLDER, filename, as_attachment=False)
    # print(imageLink)
    # return imageLink


if __name__ == '__main__':
    import os
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    get_data_imagedb()
    app.run('0.0.0.0', PORT, True)
