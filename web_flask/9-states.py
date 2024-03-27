#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page showing all states"""
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda state: state.name)

    return render_template('9-states.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a HTML page showing cities for a specific state"""
    state = storage.get("State", id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('states.html', state=state, cities=cities)
    else:
        return "<h1>Not found!</h1>"


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
