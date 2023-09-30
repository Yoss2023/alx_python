"""
Module: 1-hbnb_route

Description:
    This module contains a Flask web application with two routes.
    The application listens on 0.0.0.0 at port 5000.

Routes:
    - /: Displays "Hello HBNB!" when accessed.
    - /hbnb: Displays "HBNB" when accessed.

Usage:
    - Run this script to start the Flask application.
    - Access the / and /hbnb routes in a web browser or using curl to see the responses.

Example:
    Terminal 1:
        $ python3 1-hbnb_route.py
        * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    
    Terminal 2:
        $ curl 0.0.0.0:5000 ; echo "" | cat -e
        Hello HBNB!$
        
        $ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
        HBNB$
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

