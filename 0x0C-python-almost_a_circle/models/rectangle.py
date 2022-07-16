#!/bin/python3
"""
Module containing the rectangle class
"""


from . import base


class Rectangle(base.Base):
    """
    Rectangle class for creating and using rectangles
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialise a new Rectangle object
        Args:
            width (int): width of the Rectangle
            height (int): heightof the Rectangle
            x (int, optional): x attribute of the Rectangle
            y (int, optional): y attribute of the Rectangle
            id (int, optional): id of the Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets the width attribute
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Changes value of the width attribute
        Args:
            width (int): new width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Gets the height attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Changes value of the height attribute
        Args:
            height (int): new height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Gets the x attribute
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Changes value of the x attribute
        Args:
            x (int): new x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Gets the y attribute
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Changes value of the y attribute
        Args:
            y (int): new y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Returns the area of a Rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints a retangle to stdout
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, "#" * self.width)

    def __str__(self):
        """
        Returns humqn readable representation of rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}\
                ".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates Recatangle attributes
        Args:
        id, width, height, x, y
        """
        if len(args) == 0:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
        self.id = args[0] if len(args) > 0 else self.id
        self.width = args[1] if len(args) > 1 else self.width
        self.height = args[2] if len(args) > 2 else self.height
        self.x = args[3] if len(args) > 3 else self.x
        self.y = args[4] if len(args) > 4 else self.y

    def to_dictionary(self):
        """
        Returns dictionary representation of a Rectangle
        """
        return {"id": self.id, "width": self.width, "height": self.height,\
                "x": self.x, "y": self.y}

