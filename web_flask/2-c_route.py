#!/usr/bin/python3
"""
2-c_route.py
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


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """ C + text routing"""
    text = str(text).replace('_', ' ')
    return "C " + text


if __name__ == "__main__":
    app.run()
