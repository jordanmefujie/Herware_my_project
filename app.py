#!/usr/bin/python3
"""
"""

from flask import Flask

class Flask:
    """
    Flask class for creating Flask web applications.
    
    This class represents the Flask web application framework. It provides methods
    for creating routes, handling requests, and running the web server.
    
    Attributes:
        __name__ (str): The name of the Flask application.
    """
    
    def __init__(self, name):
        """
        Initialize a new Flask application.
        
        Args:
            name (str): The name of the Flask application.
        """
        self.__name__ = name
    
    def run(self, host='127.0.0.1', port=5000, debug=False, **options):
        """
        Run the Flask web server.
        
        Args:
            host (str): The hostname to listen on. Defaults to '127.0.0.1'.
            port (int): The port of the web server. Defaults to 5000.
            debug (bool): Whether to enable debug mode. Defaults to False.
            **options: Additional options to pass to the underlying Werkzeug server.
        """
        pass  # Method implementation is provided by the Flask module

app = Flask(__name__)

@app.route('/')
def index():
    """
    Route function for the index endpoint.
    
    Returns:
        str: A welcome message for the Herware API.
    """
    return "Welcome to the Herware API"

if __name__ == '__main__':
    app.run(debug=True)
