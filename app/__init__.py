from flask import Flask
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

import json
from flask import Flask, render_template
from flask_mqtt import Mqtt

app = Flask(__name__)


'''
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = '127.0.0.1'
app.config['MQTT_BROKER_PORT'] = 8000
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
'''


from app import routes


# initialize db connections for mongo engine, and pymongo
'''mongo_db = MongoEngine(app)
mongo.init_app(app)'''

