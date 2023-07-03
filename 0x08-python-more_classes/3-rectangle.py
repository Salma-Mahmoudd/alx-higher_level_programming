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

        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        peri = 2 * (self.__width + self.__height)
        return peri

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ((self.__height - 1) * ((self.__width * '#') + '\n'))
        return rec + (self.__width * '#')
