from flask import Flask, abort
from markupsafe import escape
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/endpoint')
def endpoint():
    return "Endpoint"

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

@app.route('/file/<checksum>', methods=["HEAD", "GET"])
def checksum(checksum):
    if request.method == "HEAD":
        abort(404)
    return checksum