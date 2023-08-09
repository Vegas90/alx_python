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
           self.id= Base.__nb_objects

"""create rectangle class inheriting from Base"""           
class Rectangle(Base):
    """class"""
    __width = 0
    __height= 0
    __x= 0
    __y= 0
     
    @property
    def width(self):
        """width""" 
        return self.__width

    @width.setter
    def width(self,width):
        """setter width"""
        width = int(width)
        if not isinstance(width,int):
            raise TypeError(f"{width} must be an integer")
        elif width <= 0:
            raise ValueError(f"{width} must be > 0")
        
        self.__width= width
    
       
    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self,height):
        """height setter"""
        if not isinstance(height,int):
            raise TypeError(f"{height} must be an integer")
        elif height <= 0:
            raise ValueError(f"{height} must be > 0")
        
        self.__height= height
    
    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self,x):
        """x setter"""
        if not isinstance(x,int):
            raise TypeError(f"{x} must be an integer")
        elif x < 0:
            raise ValueError(f"{x} must be >= 0")
      
        self.__x= x
    
    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self,y):
        """y setter"""
        if not isinstance(y,int):
            raise TypeError(f"{y} must be an integer")
        elif y < 0:
            raise ValueError(f"{y} must be >= 0")
        
        self.__y= y
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the Base class constructor with id"""
        super().__init__(id)  
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        