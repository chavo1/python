#!/usr/bin/env python3

# Exercises

# Task 1
import unittest
from typing import List

def double_preceding(values: List[float]) -> None:
    """Replace each item in the list with twice the value of the
    preceding item, and replace the first item with 0.

    >>> L = [1, 2, 3]
    >>> double_preceding(L)
    >>> L
    [0, 2, 4]
    """


    if values != []:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            values[i] = 2 * temp
            temp = values[i]

class TestDoublePreceding(unittest.TestCase):
    """Tests for double_preceding."""
    def test_identical(self):
        """Test a list with multiple identical values""" 
        argument = [1, 1, 1]
        expected = [0, 2, 2]
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list has multiple identical values.")

unittest.main()