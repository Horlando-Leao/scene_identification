from flask import Flask

app = Flask(__name__)

#cors = CORS(app, resource={r"/*": {"origins": "*"}})

from routes.Routes import *
