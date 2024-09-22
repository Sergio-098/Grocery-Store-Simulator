"""Assignment 1 - Tests for class PriorityQueue  (Task 3a)

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Joonho Kim and
Jacqueline Smith.

Module Description:
This module will contain tests for class PriorityQueue.
"""
from container import PriorityQueue


def test_remove_item() -> None:
    """test method remove"""
    pq = PriorityQueue()
    pq.add(5)
    assert pq.remove() == 5


def test_remove_item_2() -> None:
    """test method remove"""
    pq = PriorityQueue()
    pq.add(5)
    pq.add(4)
    pq.add(3)
    assert pq.remove() == 3


def test_remove_item_3() -> None:
    """test method remove"""
    pq = PriorityQueue()
    pq.add(3)
    pq.add(4)
    pq.add(3)
    assert pq.remove() == 3


def test_is_empty_on_empty() -> None:
    """Test is empty method on empty list. Should return True"""
    pq = PriorityQueue()
    assert pq.is_empty()


def test_is_empty_on_non_empty() -> None:
    """Test is empty method on non-empty list. Should return False"""
    pq = PriorityQueue()
    pq.add(3)
    assert not pq.is_empty()


def test_add_on_empty_pq() -> None:
    """Test add method when list is empty"""
    pq = PriorityQueue()
    pq.add(1)
    assert 1 in pq._items


def test_add_on_pq() -> None:
    """Test add method when list is not empty. Adds to middle of pq"""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(3)
    pq.add(2)
    assert pq._items.index(2) == 1


def test_add_to_end_pq() -> None:
    """Test add method when list is not empty. Adds to middle of pq"""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(2)
    pq.add(3)
    assert pq._items.index(3) == 2


def test_add_same() -> None:
    """Test add method when list is not empty. Adds to middle of pq"""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(2)
    pq.add(3)
    pq.add(1)
    assert pq._items[0] == 1


def test_add_same_2() -> None:
    """Test indexes of specific methods when adding equal values"""
    pq = PriorityQueue()
    pq.add('anna')
    pq.add('annaaaaa')
    pq.add('brad')
    pq.add('steven')
    pq.add('anna')
    assert 'steven' in pq._items
    assert 'brad' in pq._items
    assert pq._items[0] == 'anna'
    assert pq._items[1] == 'anna'
    assert pq._items[2] == 'annaaaaa'


if __name__ == '__main__':
    import pytest

    pytest.main(['test_priority_queue.py'])
