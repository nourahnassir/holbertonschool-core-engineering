#!/usr/init/env python3
"""Defines a class Square that inherits from Rectangle."""


class Rectangle:
    """Placeholder or base import helper."""
    pass


Rectangle = __import__('2-rectangle').Rectangle


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
