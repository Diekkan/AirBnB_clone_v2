#!/usr/bin/python3
"""
1-hbnb_route.py
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Index routing """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB routing """
    return "HBNB"


if __name__ == "__main__":
    app.run()
