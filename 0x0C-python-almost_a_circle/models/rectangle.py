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
            id: id of instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
