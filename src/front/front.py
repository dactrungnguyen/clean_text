from flask import Flask, request
from flask_restplus import Api, fields, reqparse, Resource
from werkzeug.datastructures import FileStorage

from src.back.worker import clean_text

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Clean Text service!'
