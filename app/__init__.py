from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
import paho.mqtt.client as mqtt
import time
import json

app = Flask(__name__)

from app import routes

