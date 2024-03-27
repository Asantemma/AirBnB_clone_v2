#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page showing cities by states"""
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=states_sorted)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
