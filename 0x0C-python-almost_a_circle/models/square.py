#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square:
    """Child class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class square constructor"""
        super().__init__(size, size, x, y, id)

    def __str__():
        """String method for the class square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Width property"""
        return self.width

    @size.setter
    def size(self, value):
        """Assign same value to width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method function that assigns attributes"""
        if args:
            args = (self.id, self.size, self.x, self.y)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
