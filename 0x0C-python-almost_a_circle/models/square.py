#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent a Square.
    size, x and y must be positive
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization attributes of new object.

        Args:
            size: the width of rec.
            size: the height of rec.
            x: the coordinate of rec in x axis
            y: the coordinate of rec in y axis
            id: id of instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <size>"""
        s = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return s

    @property
    def size(self):
        """get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Rectangle.

        Args:
            *args: 5 or less args
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3th argument should be the x attribute
                4th argument should be the y attribute
            **kwargs:  assigns a key/value argument to attributes
        """
        if kwargs.items():
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            j = 0
            for i in ["id", "size", "x", "y"]:
                if j < len(args):
                    setattr(self, i, args[j])
                    j += 1
                else:
                    break

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        dic = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dic
