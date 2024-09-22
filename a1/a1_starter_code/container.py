"""Assignment 1 - Container (Task 3)

CSC148 Winter 2024
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Joonho Kim and
Jacqueline Smith.

Module Description:

This file contains the classes representing the Container and Priority Queue
abstract data types.
"""

from __future__ import annotations
from typing import Any


class Container:
    """A container that holds objects.

    This is an abstract class. Only child classes should be instantiated.
    """

    def add(self, item: Any) -> None:
        """Add <item> to this Container.
        """
        raise NotImplementedError

    def remove(self) -> None:
        """Remove and return a single item from this Container.
        """
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True iff this Container is empty.
        """
        raise NotImplementedError


class PriorityQueue(Container):
    """A queue of items that operates in priority order.

    Items are removed from the queue according to priority; the item with the
    highest priority is removed first. Ties are resolved in FIFO order,
    meaning the item which was inserted *earlier* is the first one to be
    removed.

    If x < y, then x has a *HIGHER* priority than y.

    Attributes:
    - _items: The items stored in the priority queue. The highest priority item
              is at index 0.

    Representation Invariants:
    - self._items == sorted(self._items, reverse=True)
    - all objects in self._items can be compared to each other using
      comparison operators
    """
    _items: list

    def __init__(self) -> None:
        """Initialize an empty PriorityQueue.
        """
        self._items = []

    def remove(self) -> Any:
        """Remove and return the next item from this PriorityQueue.

        Precondition:
        - not self.is_empty()

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('anna')
        >>> pq.add('mona')
        >>> pq.add('hat')
        >>> pq.remove()
        'anna'
        >>> pq.remove()
        'fred'
        >>> pq.remove()
        'hat'
        >>> pq.remove()
        'mona'
        """
        return self._items.pop(0)

    def is_empty(self) -> bool:
        """
        Return True iff this PriorityQueue is empty.

        >>> pq = PriorityQueue()
        >>> pq.is_empty()
        True
        >>> pq.add('fred')
        >>> pq.is_empty()
        False
        """
        return len(self._items) == 0

    def add(self, item: Any) -> None:
        """Add <item> to this PriorityQueue.

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('anna')
        >>> pq.add('sophia')
        >>> pq.add('mona')
        >>> pq.add('anna')
        >>> pq._items
        ['anna', 'anna', 'fred', 'mona', 'sophia']
        """
        i = 0
        if self.is_empty():
            self._items.append(item)
        else:
            for x in self._items:
                if x > item:
                    self._items.insert(i, item)
                    break
                elif i == (len(self._items) - 1):
                    self._items.append(item)
                    break
                i += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    check_pyta = True
    if check_pyta:
        import python_ta
        python_ta.check_all(config={
            'allowed-import-modules': ['__future__', 'typing',
                                       'python_ta', 'doctest']})
