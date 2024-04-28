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

app.url_map.strict_slashes = False
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
