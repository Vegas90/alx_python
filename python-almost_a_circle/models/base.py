"""create class Base"""
class Base:
    """declare private variable """
    __nb_objects = 0
       
    def __init__(self, id=None):
        """if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you dont need to test the type of it"""
        if id is not None:
           self.id= id
           """otherwise, increment __nb_objects and assign the new value to the public instance attribute id"""
        else: 
           Base.__nb_objects +=1
           id= Base.__nb_objects