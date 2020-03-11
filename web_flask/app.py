from flask import Flask
from flask_pymongo import PyMongo
import json
import requests
from datetime import datetime
import pytz


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:123@mongo:27017/movie_cms'
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'This is a Flask CMS'
