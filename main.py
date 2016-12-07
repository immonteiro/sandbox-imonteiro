import base64
import json
import logging

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to sandbox, a place for potty training."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
