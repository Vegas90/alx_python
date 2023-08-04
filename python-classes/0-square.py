class MyClass:
    """
    This class represents an example class with a private instance attribute.
    """

    def __init__(self):
        """
        Constructor for MyClass.

        This method initializes the private attribute __private_attr with the value 42.
        """
        self.__private_attr = 42  # Private instance attribute

    def get_private_attr(self):
        """
        Get the value of the private attribute.

        Returns:
            int: The value of the private attribute.
        """
        return self.__private_attr

    def set_private_attr(self, value):
        """
        Set the value of the private attribute.

        Args:
            value (int): The value to set the private attribute to.
        """
        self.__private_attr = value