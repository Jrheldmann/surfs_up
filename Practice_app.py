# Import dependencies
from flask import Flask

# Create new Flask instance called "app"
app = Flask(__name__)

# Define starting point
@app.route('/')

# Create Hello World function in Flask
def hello_world():
    return 'Hello world'
