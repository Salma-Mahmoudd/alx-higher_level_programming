#!/usr/bin/python3
"""a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Represent a rectangle.
    width, height, x and y must be positive
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization attributes of new object.

        Args:
            width: the width of rec.
            height: the height of rec.
            x: the coordinate of rec in x axis
            y: the coordinate of rec in y axis
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self, x):
        """get the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self, y):
        """get the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
