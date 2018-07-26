"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, jsonify, send_from_directory, url_for, request
app = Flask(__name__, static_url_path='')
from pymongo import MongoClient
import json
import requests
import random


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


# @app.route('/image')
# def next_image():
#     one_image = images[0]
#     response = app.response_class(response=json.dumps(one_image),
#                                   status=200,
#                                   mimetype="application/json")
#     return response


@app.route('/api')
def return_image():
    imageTable = db['image']
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


# @app.route('/randomimage', methods=['GET'])
# def get_next_image():
#     key = 'authorization'
#     token = request.headers[key]
#     response = requests.get(r'https://www.googleapis.com/userinfo/v2/me', headers={key, token})
#     auth_dict = json.loads(response.text)
#     email = auth_dict['email']
#
#     users_table = db['users']
#     if email not in users_table:
#         return not_found(f'user {email}')
#     user = db.users.find({email: f'{email}'})
#
#     orgIdx = random.randint(0, len(user.organizationIds) - 1)
#     orgId = user.organizationIds[orgIdx]
#     orgs = db['organizations']
#     org = orgs[orgId]
#
#     imageIdx = random.randint(0, len(org.images) - 1)
#     image = org.images[imageIdx]
#     return jsonify({"url": image.url, "label": image.label})
#
#
# def not_found(entity):
#     resp = jsonify({'status': 404, 'message': f'{entity} not Found'})
#     resp.status_code = 404
#     return resp


@app.route('/new_label/', methods=['POST'])
def parse_post_request():
    data = request.data
    data_utf = data.decode('utf8')
    data = json.loads(data_utf)
    # data = json.dumps(data_loads, indent=4, sort_keys=True)
    print("data type: ", type(data))
    image_id = data['imageId']
    curr_label = data['originalLabel']
    new_label = data['newLabel']
    print(image_id, " , ", curr_label, ", ", new_label)
    response = app.response_class(status=200)
    return response


@app.route('/images/')
def get_all_images():
    sample = {"imageId": 123,
              "imageLink": "https://placekitten.com/600/400",
              "imageLabel": "Animal"}
    response = app.response_class(response=json.dumps(sample),
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
