from flask import Flask, json, request

app = Flask(__name__)

from routes.Routes import *

if __name__ == '__main__':
    app.run()
