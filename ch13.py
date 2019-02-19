#!/usr/bin/env python3

## Searching and Sorting

print (['d', 'a', 'b', 'a'].index('a'))


import doctest
from typing import Any
def linear_search(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    i = 0 # The index of the next item in lst to examine.
        # Keep going until we reach the end of lst or until we find value.
    while i != len(lst) and lst[i] != value: i=i+1
        # If we fell off the end of the list, we didn't find value.
    if i == len(lst): return -1
    else:
        return i
print (doctest.testmod())


#  We also need to remove it before the function exits so that the list looks unchanged to whoever called this function:

import time
import linear_search_1 
import linear_search_2 
import linear_search_3
from typing import Callable, Any
def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float: 
    """Time how long it takes to run function search to find
    value v in list L.
    """
    t1 = time.perf_counter() 
    search(L, v)
    t2 = time.perf_counter() 
    return (t2 - t1) * 1000.0
def print_times(v: Any, L: list) -> None:
    """Print the number of milliseconds it takes for linear_search(v, L) 
    to run for list.index, the while loop linear search, the for loop 
    linear search, and sentinel search.
    """
    # Get list.index's running time.
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0
    # Get the other three running times.
    while_time = time_it(linear_search_1.linear_search, L, v)
    for_time = time_it(linear_search_2.linear_search, L, v)
    sentinel_time = time_it(linear_search_3.linear_search, L, v)

    print("{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(
        v, while_time, for_time, sentinel_time, index_time))

L = list(range(10000001)) # A list with just over ten million values

print_times(10, L) # How fast is it to search near the beginning? 
print_times(5000000, L) # How fast is it to search near the middle? 
print_times(10000000, L) # How fast is it to search near the end?
    

# Binary Search

