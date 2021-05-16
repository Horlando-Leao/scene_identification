from flask_cors import CORS
from flask import Flask, json, request

app = Flask(__name__)

#cors = CORS(app, resource={r"/*": {"origins": "*"}})

from routes.Routes import *
