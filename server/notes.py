#!/usr/bin/env python3

from flask import Flask
# NOTE flask here is a class that creates an instance
# The Flask class constructor only requires the name of the primary module or package to be interpreted as the application.
app = Flask(__name__)
# __name__ here is used to inform flask where all the necessary file for our web server program is


# when clients forward requests to our applications's server they are forwarded to our FLask application instance.
# This instance will receive requests for many different resources, located at different Uniform Resource Locations (URLs). To map these URLs to Python functions, we need to define routes.
#


#easiest way to define routes with flass is through the app.route decorater

@app.route('/')
def index():
    return '<h1>welcome to my page!</h1>'

# NOTE Remember that decorators are functions that take functions as arguments and return them decorated with new features. 
# @app.route registers the index() function with the Flask application instance app

#in the cse of use wnting to retrieve something from a database we are allowed to parameterize differnet parts of our routes .... like if it was for instagram instead of hardcoding everyones usernames ... we can retrieve data from a database and simply just add it as a parameter to our function...

@app.route('/<string:username>')
def profile (username):
    return f'<h1>profile for {username}</h1>'

# ('/<username>') - dynamic ... this is a variable placeholder for our url 
#which is passed into our decorator function

# in  the terminal we are recommended to specify the flask env 
#ANCHOR - export FLASK_APP=app.py 
        # export FLASK_ENV=development   # hot reload
# export FLASK_RUN_PORT=5000     # optional


# app.run() in Flask

# app.run() starts your Flask app by:
    # Starting a development server
    #    Listens on a port (default 5000)
    # Handles incoming HTTP requests

# Serving your routes
    # Calls your functions when a URL is visited

# (Optional) Hot reload in dev mode
# If debug=True, watches files and reloads on change

from flask import flask
app = Flask(__name__)

@app.route(/<username>)
def name (username):
    return '<h1>hello<h1>'
if __name__ == '__main__':
    app.run(debug = True , port=5000)