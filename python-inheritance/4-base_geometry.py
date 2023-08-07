"""Class"""
class BaseGeometry:
    """class
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [
            item for item in attributes if item != "__innit subclass"]
        return new_attribute_list    
     """   
        
        
    def area(self):
        raise Exception ("area() is not implemented")

