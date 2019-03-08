#!/usr/bin/env python3

# Exercises

# Task 4

import unittest
class TestSorting(unittest.TestCase):
    """Tests for is_sorted.""" 
    
    def test_empty(self):
        """Test an empty list.""" 
        argument = is_sorted([])
        expected = True
        self.assertEqual(expected, argument, "The list is empty.")
    
    def test_one_item(self):
        """Test a list with one item."""
        argument = is_sorted([1])
        expected = True
        self.assertEqual(expected, argument, "The list has one item.")
    
    def test_duplicates(self):
        """Test a sorted list with duplicate values.""" 
        argument = is_sorted([1, 2, 2, 3])
        expected = True
        self.assertEqual(expected, argument, "The list has duplicate values.")
    
    def test_not_sorted(self):
        """Test an unsorted list.""" 
        argument = is_sorted([3, 2])
        expected = False
        self.assertEqual(expected, argument, "The list has one item.")

unittest.main()