"""
declare class

"""

class Square:

    """
adds up

"""
    def __init__(self,size = 0):
       if type(size) is not int:
           raise TypeError("size must be an integer")
       elif size < 0:
           raise ValueError("size must be >= 0")
       else:
           self.__size=size
    
    def area(self):
        return self.__size ** 2