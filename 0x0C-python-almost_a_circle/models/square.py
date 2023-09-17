#!/usr/bin/python3
"""
Module contains class square inherits class base
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    inherited attributes __width, __height, __x and __y
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width
    @size.setter
    def size(self, val):
        """size setter"""
        self.width = val
        self.height = val
