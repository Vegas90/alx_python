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