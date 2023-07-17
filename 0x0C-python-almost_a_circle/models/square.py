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
