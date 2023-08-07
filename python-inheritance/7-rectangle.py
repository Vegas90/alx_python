"""Class"""
class BaseGeometry():
    """class
    
     """
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list =[
            item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
     
            
    def area(self):
        """class"""
        raise Exception ("area() is not implemented")
    """class"""
    #@area.setter
        #"""class"""
    def integer_validator(self, name, value):
        """class"""
        if not isinstance(value, int):
            """class"""
            raise TypeError(f"{name} must be an integer")
        elif value == 0 :
            """Class"""
            raise ValueError(f"{name} must be greater than 0")
        else:
            """Class"""
            return value
        
        
class Rectangle(BaseGeometry):
    """class"""
    def __init__(self, width, height):
        """class"""
        self.__width = super().integer_validator("width",width)
        self.__height = super().integer_validator("height", height)
        
    def area(self):
        return self.__width * self.__height
    
    def print(self):
        print(self.area())
    
    def __str__(self):
        return "Rectangle <{self.__width}>/<{self.__height}>"