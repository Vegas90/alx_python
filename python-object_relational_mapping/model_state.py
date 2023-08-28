#!/usr/bin/python
""" 
contains state class and ......
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

# Create a database connection using command line arguments
engine = create_engine(f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

# Create a base class for declarative models
Base = declarative_base()

class State(Base):
    """
    Represents a state in the 'states' table.
    
    Attributes:
        id (int): The primary key identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

# Create the tables in the database
Base.metadata.create_all(engine)

