"""Class"""
class BaseGeometry:
    """class
    
     """       
    def area(self):
        raise Exception ("area() is not implemented")
    """class
    
     """
    @area.setter
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError(f"{name}must be an integer")
        elif value < 0 :
            raise ValueError(f"{name} must be greater than 0")
        else:
            return value