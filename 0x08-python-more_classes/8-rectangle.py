#!/usr/bin/python3
"""A class that represents a rectangle"""


class Rectangle:
    """Define a rectangle with private attributes: width, height"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        A new object.

        Args:
            width: width of rectangle.
            height: height of rectangle.
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        s = str(self.print_symbol)
        rec = ((self.__height - 1) * ((self.__width * s) + '\n'))
        return rec + (self.__width * s)

    def __repr__(self):
        repr = f"Rectangle({self.__width}, {self.__height})"
        return repr

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
