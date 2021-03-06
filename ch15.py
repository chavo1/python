#!/usr/bin/env python3

# Testing and Debugging

def above_freezing(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.
    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """
    return celsius > 0

def above_freezing_v2(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.
    >>> above_freezing_v2(5.2)
    True
    >>> above_freezing_v2(-2)
    False
    """
    return celsius >= 0


# Code look similar but result is not the same
print(above_freezing(0))
print(above_freezing_v2(0))

# First test class

import unittest 
import temperature
class TestAboveFreezing(unittest.TestCase): 
    """Tests for temperature.above_freezing."""
    def test_above_freezing_above(self):
        """Test a temperature that is above freezing."""
        expected = True
        actual = temperature.above_freezing(5.2)
        self.assertEqual(expected, actual,
            "The temperature is above freezing.") 
    def test_above_freezing_below(self):
        """Test a temperature that is below freezing."""
        expected = False
        actual = temperature.above_freezing(-2)
        self.assertEqual(expected, actual,
            "The temperature is below freezing.") 
    def test_above_freezing_at_zero(self):
        """Test a temperature that is at freezing."""
        expected = False
        actual = temperature.above_freezing(0)
        self.assertEqual(expected, actual,
            "The temperature is at the freezing mark.")
            
unittest.main()

# Exercises

# Task 1

from typing import List
def double_preceding(values: List[float]) -> None:
    """Replace each item in the list with twice the value of the preceding item, and replace the first item with 0.
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

