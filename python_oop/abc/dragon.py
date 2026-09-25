#!/usr/bin/env python3
"""Defines SwimMixin, FlyMixin, and a Dragon class combining both behaviors."""


class SwimMixin:
    """Provides swimming capability."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying capability."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a Dragon inheriting from SwimMixin and FlyMixin."""

    def roar(self):
        """Prints the dragon's roar."""
        print("The dragon roars!")
