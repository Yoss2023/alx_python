"""
Module: 0-hello_route

Description:
    This module contains a simple Flask web application with a single route.
    The application listens on 0.0.0.0 at port 5000.

Routes:
    - /: Displays "Hello HBNB!" when accessed.

Usage:
    - Run this script to start the Flask application.
    - Access the / route in a web browser or using curl to see the response.

Example:
    Terminal 1:
        $ python3 0-hello_route.py
        * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    
    Terminal 2:
        $ curl 0.0.0.0:5000 ; echo "" | cat -e
        Hello HBNB!$
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

