#!/usr/bin/python3
"""Base class"""


import json
import csv
from os import path


class Base:
    """Base class"""
    __nb_objects = 0

    def reset_objects():
        """Initialize sdnads alksdn al"""
        Base.__nb_objects = 0

    def __init__(self, id=None):
        """Initialize sdnads alksdn al"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Initialize sdnads alksdn al"""
        list_dictionaries = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
                file.write(Base.to_json_string(list_dictionaries))
            return
        for model in list_objs:
            list_dictionaries.append(model.to_dictionary())
        with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
            file.write(Base.to_json_string(list_dictionaries))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Initialize sdnads alksdn al"""
        with open(cls.__name__ + ".csv", "w", newline='') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            if list_objs is not None:
                for model in list_objs:
                    writer.writerow(model.to_dictionary())

    @staticmethod
    def to_json_string(list_dictionaries):
        """Initialize sdnads alksdn al"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Initialize sdnads alksdn al"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Initialize sdnads alksdn al"""
        if cls.__name__ == "Rectangle":
            object = cls(1, 1)
            object.update(**dictionary)
            return object

        if cls.__name__ == "Square":
            object = cls(1)
            object.update(**dictionary)
            return object

    @classmethod
    def load_from_file(cls):
        """Initialize sdnads alksdn al"""
        if path.exists(cls.__name__ + ".json") is False:
            return []
        with open(cls.__name__ + ".json", "r",  encoding='utf-8') as file:
            listofinstances = []
            objectlist = cls.from_json_string(file.read())
            for dict in objectlist:
                objectdict = {}
                for key, value in dict.items():
                    objectdict[key] = value
                listofinstances.append(cls.create(**objectdict))
            return listofinstances

    @classmethod
    def load_from_file_csv(cls):
        """Initialize sdnads alksdn al"""
        if path.exists(cls.__name__ + ".csv") is False:
            return []
        with open(cls.__name__ + ".csv", "r", newline='') as f:
            listofinstances = []
            reader = csv.DictReader(f)
            for row in reader:
                for key, value in row.items():
                    row[key] = int(value)
                listofinstances.append(cls.create(**row))
        return listofinstances
