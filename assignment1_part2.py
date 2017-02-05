#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: assignment1_part2.py."""


class Book(object):
    """A Book class definition.

    Attributes:
        author (string): A class attribute of Book. Defaults to empty string.
        title (string): A class attribute of Book. Defaults to empty string.
    """
    author = ''
    title = ''

    def __init__(self, input_author='', input_title=''):
        """Constructor for the Book() class.

        Args:
            input_author (string, optional): The Book Author. Defaults to empty
            string.
            input_title (string, optional): The Book Title. Defaults to empty
            string.

        Attributes:
            author (string): A pseudo-private attribute assigned to the
            constructor variable file_path.
            title (string): A pseudo-private attribute assigned to the
            constructor variable file_path2.
        """
        self.author = input_author
        self.title = input_title

    def display(self):
        """A function that prints out a string representing the book.

        Args:
            None.

        Returns:
            None

        Examples:

            >>> a = Book('John Steinbeck','Of Mice and Men')
            >>> a.display()
            Of Mice and Men, written by John Steinbeck
        """
        print self.title + ", written by", self.author
