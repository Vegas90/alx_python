#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

#create instance of this class
@app.route("/",strict_slashes=False)
#returns messages we want to display
def hello():
    #returns
    return "Hello HBNB!"

#You must use the option strict_slashes=False in your route definition
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)