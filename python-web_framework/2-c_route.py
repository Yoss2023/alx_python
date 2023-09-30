"""
Module: 2-c_route

Description:
    This module contains a Flask web application with three routes.
    The application listens on 0.0.0.0 at port 5000.

Routes:
    - /: Displays "Hello HBNB!" when accessed.
    - /hbnb: Displays "HBNB" when accessed.
    - /c/<text>: Displays "C " followed by the value of the text variable. Underscores (_) are replaced with spaces.

Usage:
    - Run this script to start the Flask application.
    - Access the /, /hbnb, and /c/<text> routes in a web browser or using curl to see the responses.

Examples:
    Terminal 1:
        $ python3 2-c_route.py
        * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    
    Terminal 2:
        $ curl 0.0.0.0:5000 ; echo "" | cat -e
        Hello HBNB!$
        
        $ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
        HBNB$
        
        $ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
        C is fun$
        
        $ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
        C cool$
        
        $ curl 0.0.0.0:5000/c ; echo "" | cat -e
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

