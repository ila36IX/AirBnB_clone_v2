#!/usr/bin/python3
"""
Web application listens on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    """Display Hello"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """Handle link input"""
    return "c " + text.replace("_", " ")


@app.route("/python/<text>")
@app.route("/python/")
@app.route("/python")
def python_is_cool(text=None):
    """Handle link input"""
    if not text:
        text = "is cool"
    return "python " + text.replace("_", " ")


app.url_map.strict_slashes = False
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
