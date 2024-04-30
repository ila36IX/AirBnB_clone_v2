#!/usr/bin/python3
"""
Web application listens on 0.0.0.0, port 5000
Getting data from db
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list")
def hello_db(n=None):
    """Display the states in the db"""
    states = storage.all(State)
    states = sorted(states.values(), key= lambda s: s.name.lower())
    temp_file = "7-states_list.html"
    return render_template(temp_file, states=states)


@app.teardown_appcontext
def reloading(e):
    """releasing any connection resources owned by session"""
    storage.close()


app.url_map.strict_slashes = False
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
