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

    @property
    def height(self):
        """get the height"""
        return self.__height

    @property
    def x(self, x):
        """get the x"""
        return self.__x

    @property
    def y(self, y):
        """get the y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set the x"""
        if type(value) != int:
            raise TypeError("x  must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set the y"""
        if type(value) != int:
            raise TypeError("y  must be an integer")
        if value < 0:
            raise ValueError("y  must be >= 0")
        self.__y = value

    def area(self):
        """Area of rec"""
        area = self.__width * self.__height
        return area

    def display(self):
        """ prints the Rectangle instance with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        s = "#"
        rec = ((self.__height - 1)*((' '*self.__y)+(self.__width * s)+'\n'))
        print("\n" * self.__y, end="")
        print(f"{rec + ((' '*self.__y)+self.__width * s)}")

    def __str__(self):
        s = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
        return f"{s}{self.__width}/{self.__height}"

    def update(self, *args):
        j = 0
        for i in ["id", "width", "height", "x", "y"]:
            if j < len(args):
                setattr(self, i, args[j])
                j += 1
            else:
                break
