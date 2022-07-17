#!/usr/bin/python3
"""
Module contqining the Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class for creating and working with squares
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialise a new Square object
        Args:
            width (int): size of the Square
            x (int, optional): x attribute of the Square
            y (int, optional): y attribute of the Square
            id (int, optional): id of the Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a human readable format of Square
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Gets the size attribute
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Changes value of the width attribute
        Args:
            size (int): new size
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Extends Rectangle update function
        """
        if len(args) == 0:
            id = kwargs.get("id", self.id)
            size = kwargs.get("size", self.size)
            x = kwargs.get("x", self.x)
            y = kwargs.get("y", self.y)
            super().update(id=id, width=size, height=size, x=x, y=y)
        super().update(
                args[0] if len(args) > 0 else self.id,
                args[1] if len(args) > 1 else self.size,
                args[1] if len(args) > 1 else self.size,
                args[2] if len(args) > 2 else self.x,
                args[3] if len(args) > 3 else self.y,
                )

    def to_dictionary(self):
        """
        Returns dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
