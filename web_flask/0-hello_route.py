#!/usr/bin/python3
"""
0-hello_route.py
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Index routing """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
