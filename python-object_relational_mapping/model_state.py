# Create a database connection
from sqlalchemy import create_engine, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
# Create a database connection
engine = create_engine('mysql://argv[1]:argv[2]@localhost:3306/argv[3]')
#create base class
Base = declarative_base()
#defined mapped class
class State(Base):
    #defined mapped class
    __tablename__= 'states'
    #defined mapped class
    id= Column(Integer, primary_key=True, autoincrement=True)
    #defined mapped class
    name = Column(String(128),nullable=False)
     
# Import other mapped classes before create_all
Base.metadata.create_all(engine)
