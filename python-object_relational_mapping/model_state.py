# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, argv
from sqlalchemy.ext.declarative import declarative_base
# Create a database connection using command line arguments
engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
# Create a base class for declarative models
Base = declarative_base()
# Define a mapped class named 'State'
class State(Base):
    # Specify the name of the table in the database
    __tablename__ = 'states'
    # Define attributes for the 'states' table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

# Create the tables in the database
Base.metadata.create_all(engine)