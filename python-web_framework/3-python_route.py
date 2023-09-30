"""
Module: 3-python_route

Description:
    This module contains a Flask web application with four routes.
    The application listens on 0.0.0.0 at port 5000.

Routes:
    - /: Displays "Hello HBNB!" when accessed.
    - /hbnb: Displays "HBNB" when accessed.
    - /c/<text>: Displays "C " followed by the value of the text variable. Underscores (_) are replaced with spaces.
    - /python/<text>: Displays "Python " followed by the value of the text variable. Underscores (_) are replaced with spaces.
        The default value of text is "is cool".

Usage:
    - Run this script to start the Flask application.
    - Access the /, /hbnb, /c/<text>, and /python/<text> routes in a web browser or using curl to see the responses.

Examples:
    Terminal 1:
        $ python3 3-python_route.py
        * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    
    Terminal 2:
        $ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
        Python is magic$
        
        $ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
        Python is cool$
        
        $ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
        Python is cool$
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the / route.

    Returns:
        str: "Hello HBNB!"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the /hbnb route.

    Returns:
        str: "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route handler for the /c/<text> route.

    Args:
        text (str): The text variable in the route.

    Returns:
        str: "C " followed by the value of the text variable. Underscores (_) are replaced with spaces.
    """
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Route handler for the /python/<text> route.

    Args:
        text (str): The text variable in the route.

    Returns:
        str: "Python " followed by the value of the text variable. Underscores (_) are replaced with spaces.
    """
    return "Python " + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

