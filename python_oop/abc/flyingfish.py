#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classes demonstrating multiple inheritance."""


class Fish:
    """Represents a fish with swimming and habitat behaviors."""

    def swim(self):
        """Prints the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying and habitat behaviors."""

    def fly(self):
        """Prints the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish inheriting from both Fish and Bird."""

    def fly(self):
        """Overrides fly method for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides swim method for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat method for flying fish."""
        print("The flying fish lives both in water and the sky!")
