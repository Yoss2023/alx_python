"""
Module: 5-number_template

Description:
    This module contains a Flask web application with six routes.
    The application listens on 0.0.0.0 at port 5000.

Routes:
    - /: Displays "Hello HBNB!" when accessed.
    - /hbnb: Displays "HBNB" when accessed.
    - /c/<text>: Displays "C " followed by the value of the text variable. Underscores (_) are replaced with spaces.
    - /python/<text>: Displays "Python " followed by the value of the text variable. Underscores (_) are replaced with spaces.
        The default value of text is "is cool".
    - /number/<n>: Displays "{n} is a number" only if n is an integer.
    - /number_template/<n>: Displays an HTML page only if n is an integer. The page includes an H1 tag with "Number: n" inside the BODY tag.

Usage:
    - Run this script to start the Flask application.
    - Access the /, /hbnb, /c/<text>, /python/<text>, /number/<n>, and /number_template/<n> routes in a web browser or using curl to see the responses.

Examples:
    Terminal 1:
        $ python3 5-number_template.py
        * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    
    Terminal 2:
        $ curl 0.0.0.0:5000/number_template/89 ; echo ""
        <!DOCTYPE html>
        <HTML lang="en">
            <HEAD>
                <TITLE>HBNB</TITLE>
            </HEAD>
            <BODY>
                <H1>Number: 89</H1>
            </BODY>
        </HTML>

        $ curl 0.0.0.0:5000/number_template/8.9 
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.

        $ curl 0.0.0.0:5000/number_template/python 
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.
"""

from flask import Flask, render_template

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
        str: "{} is a number" if n is an integer.
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for the /number_template/<n> route.

    Args:
        n (int): The number variable in the route.

    Returns:
        HTML: An HTML page with an H1 tag containing "Number: n" inside the BODY tag.
    """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

