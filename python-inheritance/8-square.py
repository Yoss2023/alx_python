#!/usr/bin/python3

""" Module for the Square class."""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):

    """ Square class, inherits from Rectangle."""

    def __init__(self, size):
    
    """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
    
        """ Compute the area of the square."""
        
        return self.__size ** 2

    def __str__(self):
        
        """ Return a string representation of the Square."""
        
        return "[Square] {}/{}".format(self.__size, self.__size)

    @property
    def size(self):
        
        """ Getter for the size attribute."""
        
        return self.__size

