#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: assignment1_part1.py."""


def listDivide(numbers, divide=2):
    """A function that returns the number of elements in the numbers list that
        are divisible by divide.

    Args:
        numbers(list): A list of numbers.
        divide(integer): An integer used in division. Defaults to 2.

    Returns:
        integer: The number of elements in the list that are divisible by
        divide.

    Examples:

        >>> listDivide([1,2,3,4,5])
        2
    """
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1

    return count


class ListDivideException(Exception):
    """A Custom Exception object."""
    pass


def testListDivide():
    """A function that performs tests on listDivide.

    Args:
        None.
    """
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException

    if listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException

    if listDivide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException

    if listDivide([]) != 0:
        raise ListDivideException

    if listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException
