"""
Module: 4-number_route

Description:
    This module contains a Flask web application with five routes.
    The application listens on 0.0.0.0 at port 5000.

Routes:
    - /: Displays "Hello HBNB!" when accessed.
    - /hbnb: Displays "HBNB" when accessed.
    - /c/<text>: Displays "C " followed by the value of the text variable. Underscores (_) are replaced with spaces.
    - /python/<text>: Displays "Python " followed by the value of the text variable. Underscores (_) are replaced with spaces.
        The default value of text is "is cool".
    - /number/<n>: Displays "n is a number" only if n is an integer.

Usage:
    - Run this script to start the Flask application.
    - Access the /, /hbnb, /c/<text>, /python/<text>, and /number/<n> routes in a web browser or using curl to see the responses.

Examples:
    Terminal 1:
        $ python3 4-number_route.py
        * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    
    Terminal 2:
        $ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
        89 is a number$

        $ curl 0.0.0.0:5000/number/8.9 
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.

        $ curl 0.0.0.0:5000/number/python 
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.
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

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route handler for the /number/<n> route.

    Args:
        n (int): The number variable in the route.

    Returns:
        str: "{n} is a number" if n is an integer, otherwise a 404 Not Found response.
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

