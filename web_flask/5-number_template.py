#!/usr/bin/python3
"""
5-number_template.py
"""
from flask import Flask, abort, render_template
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


@app.route('/number/<n>', strict_slashes=False)
def isanumber(n):
    """ returns if isanumber """
    if n.isnumeric():
        return str(n) + " is a number"
    else:
        return abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def numbertemplate(n):
    """ returns template if isanumber """
    if n.isnumeric():
        return render_template("5-number.html", number=n)
    else:
        return abort(404)


if __name__ == "__main__":
    app.run()
