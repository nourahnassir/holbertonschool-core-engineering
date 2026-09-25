#!/usr/bin/env python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print and str representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
