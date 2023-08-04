"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

"""
class Square:
#python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    def __init__(self,size):
        size = self.__size