"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, jsonify, send_from_directory, url_for
app = Flask(__name__, static_url_path='')
from apis import get_data_imagedb


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


if __name__ == '__main__':
    import os
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    get_data_imagedb()
    app.run('0.0.0.0', PORT, True)
    print("does the flow go here?")
