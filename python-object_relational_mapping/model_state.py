# Specify the name of the table in the database
from sqlalchemy import create_engine, Column, Integer, String, argv
from sqlalchemy.ext.declarative import declarative_base

# Create a database connection using command line arguments
engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

#Create a base class for declarative models
Base = declarative_base()

"""
Define a mapped class named 'State'
python3 -c 'print(__import__("my_module").MyClass.__doc__)"""
class State(Base):
    # Specify the name of the table in the database
    __tablename__ = 'states'
    # Define attributes for the 'states' table
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Define a mapped class named 'State'
    name = Column(String(128), nullable=False)

# Create the tables in the database
Base.metadata.create_all(engine)