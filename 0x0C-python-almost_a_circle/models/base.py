#!/usr/bin/python3
"""Base class"""
import json


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
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        File = cls.__name__ + ".json"
        with open(File, 'w') as jfile:
            if list_objs is not None:
                list = []
                for i in list_objs:
                    list.append(i.to_dictionary())
                jfile.write(Base.to_json_string(list))
            else:
                jfile.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is not None:
            return json.loads(json_string)
        return "[]"
