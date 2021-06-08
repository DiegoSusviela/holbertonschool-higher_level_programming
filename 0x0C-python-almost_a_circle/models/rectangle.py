#!/usr/bin/python3
"""read_file function"""


from models.base import Base


class Rectangle(Base):
    """Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Base class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Base class"""
        return self.__width

    @property
    def height(self):
        """Base class"""
        return self.__height

    @property
    def x(self):
        """Base class"""
        return self.__x

    @property
    def y(self):
        """Base class"""
        return self.__y

    @width.setter
    def width(self, value):
        """Base class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Base class"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Base class"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Base class"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Base class"""
        return self.__width * self.__height

    def display(self):
        """Base class"""
        print(("\n" * self.__y) + "\n".join(((" " * self.__x) +
                                            ("#" * self.__width))
                                            for i in range(self.__height)))

    def __str__(self):
        """Base class"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """Base class"""
        if len(args):
            for i, x in enumerate(args):
                if i == 0:
                    self.id = x
                elif i == 1:
                    self.width = x
                elif i == 2:
                    self.height = x
                elif i == 3:
                    self.x = x
                elif i == 4:
                    self.y = x
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Base class"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
