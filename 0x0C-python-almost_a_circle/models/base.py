#!/usr/bin/python3
"""
Base class module
"""


import json


class Base:
    """
    The base class aims to manage id
    """
    __nb_object = 0

    def __init__(self, id=None):
        """
        initialise Base class
        Args:
            id (int): The object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json string representation of list_objs to a
        file named <Class name>.json
        Args:
            list_objs (list): liat of objects
        """
        fileName = cls.__name__ + ".json"
        list_dict_objs = [obj.to_dictionary() for obj in list_objs]
        with open(fileName, "w") as myFile:
            json.dump(list_dict_objs, myFile)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries for the JSON string representation
        Args:
            json_string (str): JSON string representation of object
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
            dictionary (dict) : dict of attributes
        """
        newInstance = cls(4, 5)
        newInstance.update(**dictionary)
        return newInstance

    @classmethod
    def load_from_file(cls):
        """
        Read from file <Class name>.json and Returns a list of instances 
        """
        instanceList = []
        with open(cls.__name__ + ".json", "r") as myFile:
            dictList = cls.from_json_string(myFile.read())
        for i in dictList:
            instanceList.append(cls.create(**i))
        return instanceList
