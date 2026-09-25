#!/usr/bin/env python3
"""Defines a class Square that inherits from Rectangle."""

Rectangle = __import__('1-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
