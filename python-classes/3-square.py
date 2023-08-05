"""
declare class

"""

class Square:

    """
adds up

"""

    def __init__(self,size = 0):
        """The @property decorator allows you to access the size attribute like an attribute"""
        @property
        def size(self):
            return self.__size
    
        """@size.setter decorator allows you to set the size attribute while performing the necessary checks for type and value constraints. 
        """
        @size.setter
        def size(self,value):
                if type(value) is not int:
                    raise TypeError("size must be an integer")
                elif value < 0:
                 raise ValueError("size must be >= 0")
                else:
                 self.__size= value
    
   
    def area(self):
         return self.__size ** 2