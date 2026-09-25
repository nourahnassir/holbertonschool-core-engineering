#!/usr/init/env python3
"""Defines an abstract class Shape and concrete subclasses Circle and Rectangle."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Represents an abstract shape class."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """Represents a Circle subclass inheriting from Shape."""

    def __init__(self, radius):
        """Initializes a new Circle.

        Args:
            radius (float/int): The radius of the circle.
        """
        self.__radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Returns the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Represents a Rectangle subclass inheriting from Shape."""

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
            width (float/int): The width of the rectangle.
            height (float/int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    """Prints the area and perimeter of a given shape object using duck typing."""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
