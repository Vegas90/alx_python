"""Class"""
class BaseGeometry:
    """class"""

@property
def area(self):
    return self

@area.setter
def area(self,value):
    self.__value= value
    raise Exception("area() is not implemented")
