#!/usr/bin/python3
"""
3-python_route.py
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythontext(text='is cool'):
    """ Python + text routing"""
    text = str(text).replace('_', ' ')
    return "Python " + text


if __name__ == "__main__":
    app.run()
