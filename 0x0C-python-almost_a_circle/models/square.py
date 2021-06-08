#!/usr/bin/python3
""""Square" class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Base class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Base class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Base class"""
        return self.width

    @size.setter
    def size(self, value):
        """Base class"""
        self.width = value
        self.height = value

    def __str__(self):
        """Base class"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """Base class"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Base class"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
