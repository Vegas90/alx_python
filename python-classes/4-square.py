"""
declare class

"""

class Square:

    """
adds up

"""

    def __init__(self,size = 0):
        self.__size = size
        
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
    
    def my_print(self):
        if self.__size ==0:
           print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                else:
                    print("\n") 
                