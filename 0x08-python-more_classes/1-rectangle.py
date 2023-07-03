#!/usr/bin/python3
"""A class that represents a rectangle"""


class Rectangle:
    """Define a rectangle with private attributes: width, height"""

    def __init__(self, width=0, height=0):
        """
        A new object.

        Args:
            width: width of rectangle.
            height: height of rectangle.
        """

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get a private attribute of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set a private attribute of width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get a private attribute of height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set a private attribute of height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
