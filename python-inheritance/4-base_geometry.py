"""Class"""
class BaseGeometry:
    """class"""
def __init__(self, area="Unknown"):
    self.__area = area
@property
def area(self):
    return self

@area.setter
def area(self,value):
    self.__value= value
    raise Exception("area() is not implemented")
