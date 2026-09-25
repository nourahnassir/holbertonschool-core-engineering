#!/usr/bin/env python3
"""Defines an abstract class Animal and concrete subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Represents an abstract animal class."""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound."""
        pass


class Dog(Animal):
    """Represents a Dog subclass inheriting from Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represents a Cat subclass inheriting from Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
