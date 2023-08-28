#!/usr/bin/python
""" 
contains state class and ......
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

# Create a database connection using command line arguments
engine = create_engine(f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')
 # Create a configured "Session" class
Session = sessionmaker(bind=engine)
# Create a Session
session = Session()
# Query the State table and order the results by id in ascending order
states = session.query(State).order_by(State.id).first()

# Display the result
if 'a' in states.name:
    for state in states:
        print(f"{states.id}: {states.name}")
else:
    print("Nothing")
        
# Close the session
session.close()


