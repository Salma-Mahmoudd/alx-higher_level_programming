#!/usr/bin/python3
"""function that adds a new attribute"""


def add_attribute(obj, attribute, value):
    """check if we can or not"""

    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
