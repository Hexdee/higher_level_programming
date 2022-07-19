#!/usr/bin/python3
"""
Base class module
"""


import os
import json


class Base:
    """
    The base class aims to manage id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialise Base class
        Args:
            id (int): The object id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json string representation of list_objs to a
        file named <Class name>.json
        Args:
            list_objs (list): list of objects
        """
        fileName = cls.__name__ + ".json"
        if list_objs is not None:
            list_dict_objs = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dict_objs = []
        list_str_obj = cls.to_json_string(list_dict_objs)
        with open(fileName, "w") as myFile:
            myFile.write(list_str_obj)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries for the JSON string representation
        Args:
            json_string (str): JSON string representation of object
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
            dictionary (dict) : dict of attributes
        """
        if cls.__name__ == "Square":
            newInstance = cls(4)
        elif cls.__name__ == "Rectangle":
            newInstance = cls(4, 4)
        newInstance.update(**dictionary)
        return newInstance

    @classmethod
    def load_from_file(cls):
        """
        Read from file <Class name>.json and Returns a list of instances
        """
        instanceList = []
        if not os.path.isfile(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as myFile:
            content = myFile.read()
        if content == "":
            return []
        dictList = cls.from_json_string(content)
        for i in dictList:
            instanceList.append(cls.create(**i))
        return instanceList
