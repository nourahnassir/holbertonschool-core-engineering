#!/usr/bin/env python3
"""Defines a VerboseList class that extends the built-in list class with notifications."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        """Adds an item to the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with items from an iterable and prints a notification."""
        initial_len = len(self)
        super().extend(iterable)
        added_count = len(self) - initial_len
        print(f"Extended the list with [{added_count}] items.")

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
