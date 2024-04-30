#!/usr/bin/python3
"""
Web application listens on 0.0.0.0, port 5000
Getting data from db
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states")
def hello_db():
    """Display the states in the db"""
    states = storage.all(State).values()
    temp_file = "9-states.html"
    return render_template(temp_file, states=states)


@app.route("/states/<id>")
def state_id(id):
    """Display the state with the id"""
    states = storage.all(State)
    state_info = states.get(f"State.{id}")
    temp_file = "9-states.html"
    return render_template(
        temp_file,
        state_info=state_info
    )


@app.teardown_appcontext
def reloading(e):
    """releasing any connection resources owned by session this will make sure
    that all changes that heppend in the time of request are not lost
    """
    storage.close()


app.url_map.strict_slashes = False
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
