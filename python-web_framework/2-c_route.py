#!/usr/bin/python
"""
A script that starts a flas web application:
Listening on 0.0.0.0 port 5000
Routes: /display "Hello HBNB!"
"""
from flask import Flask
app = Flask(__name__)

@app.route("/",strict_slashes=False)
def hello():
   """
   This function returns the specified string when the text in that directory
   """
   return "Hello HBNB!"

@app.route("/hbnb",strict_slashes=False)
def hellow():
   """
   This function returns the specified string when the text in that directory
   """
   return "HBNB"

@app.route("/c/<text>",strict_slashes=False)
def c(text):
   """
   This function returns the specified string when the text in that directory
   """
   return f"C {text}"

#You must use the option strict_slashes=False in your route definition
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)