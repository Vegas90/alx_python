from sqlalchemy import create_engine, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a database connection
engine = create_engine('mysql://argv[1]:argv[2]@localhost:3306/argv[3]')

#create base class
Base = declarative_base()

#defined mapped class
class State(Base):
    __tablename__= 'states'
    
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128),nullable=False)
     
# Import other mapped classes before create_all
# class OtherClass(Base):
# Create tables
Base.metadata.create_all(engine)
