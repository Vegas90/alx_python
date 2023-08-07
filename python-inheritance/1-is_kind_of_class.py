"""
check a true
"""
def is_kind_of_class(obj, a_class):
    """
This function will return True if the object is an instance of the specified main class or any class derived from the same main class.
"""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)