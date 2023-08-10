from models.rectangle import Rectangle

"""class"""
class Square(Rectangle):
    """frp, rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
         """initialize the inherited values"""
         super().__init__(size,x=0, y=0, id = None)
         
    def __str__(self):
        """rectangle"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
       