#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class has id for each object"""
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
