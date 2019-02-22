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



# Timing the Searches

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
    
# binary search


from typing import Any
def binary_search(L: list, v: Any) -> int:
    """Return the index of the first occurrence of value in L, or return 
    -1 if value is not in L.
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 1)
    0
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 4)
    2
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 5)
    4
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 10)
    7
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], -3)
    -1
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 11)
    -1
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 2)
    -1
    >>> binary_search([], -3)
    -1
    >>> binary_search([1], 1)
    0
    """
    # Mark the left and right indices of the unknown section.
    i=0
    j = len(L) - 1
    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v: 
            i=m+1
        else: 
            j=m-1
    if 0 <= i < len(L) and L[i] == v: 
        return i
    else:
        return -1
if __name__ == '__main__': 
    import doctest
    print(doctest.testmod())


# Sorting

import time
import random
from sorts import selection_sort 
from sorts import insertion_sort
def built_in(L: list) -> None:
    """Call list.sort --- we need our own function to do this so that we can 
    treat it as we treat our own sorts.
    """
    L.sort()
def print_times(L: list) -> None:
    """Print the number of milliseconds it takes for selection 
    sort, insertion sort, and list.sort to run.
    """
    print(len(L), end='\t')
    for func in (selection_sort, insertion_sort, built_in):
        if func in (selection_sort, insertion_sort) and len(L) > 10000: 
            continue
        L_copy = L[:]
        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()
        print("{0:7.1f}".format((t2 - t1) * 1000.), end='\t')
    print() # Print a newline.
for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]: 
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)

# More Efficient Sorting Algorithms

import bisect
def bin_sort(values: list) -> list:
    """Return a sorted version of the values. (This does not mutate values.) 
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bin_sort(L)
    [-1, 2, 3, 4, 5, 7]
    """
    result = []
    for v in values:
        bisect.insort_left(result, v) 
    return result 

if __name__ == '__main__': 
    import doctest
    print(doctest.testmod())

# Merging Two Sorted Lists


## i1 and i2 are the indices into L1 and L2, respectively; in each iteration, 
# we compare L1[i1] to L2[i2] and copy the smaller item to the resulting list.
#  At the end of the loop, we have run out of items in one of the two lists, 
# and the two extend calls will append the rest of the items to the result.

def merge(L1: list, L2: list) -> list:
    """Merge sorted lists L1 and L2 into a new list and return that new list. 
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """
    newL = []
    i1 = 0
    i2 = 0
    # For each pair of items L1[i1] and L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2): 
        if L1[i1] <= L2[i2]:
                newL.append(L1[i1])
                i1 += 1 
        else:
                newL.append(L2[i2])
                i2 += 1
    # Gather any leftover items from the two sections.
    # Note that one of them will be empty because of the loop condition. 
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL

if __name__ == '__main__': 
    import doctest
    print(doctest.testmod())

# Merge Sort

def mergesort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    # Make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(L)):
            workspace.append([L[i]])
        # The next two lists to merge are workspace[i] and workspace[i + 1].
    i=0
        # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1: 
        L1 = workspace[i]
        L2 = workspace[i + 1] 
        newL = merge(L1, L2) 
        workspace.append(newL)
        i += 2
    # Copy the result back into L.
    if len(workspace) != 0: L[:] = workspace[-1][:]

if __name__ == '__main__': 
    import doctest
    print(doctest.testmod())


  
  # Exercises CH13


# Task 1
# All three versions of linear search start at index 0. Rewrite all to search from
# the end of the list instead of from the beginning. Make sure you test them.
# 1
# While loop

def linear_search(lst, value):
    """ (list, object) -> int

    Return the index of the last occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    2
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """ 

    i = len(lst) -1  # The index of the next item in lst to examine.
    
    # Keep going until we reach the end of lst or until we find value.
    while i != -1 and lst[i] != value:
        i = i - 1
    
    # If we fell off the end of the list, we didn't find value.
    if i == -1:
        return -1
    else:
        return i

if __name__ == '__main__': 
    import doctest
    print(doctest.testmod())

# 2
# For loop

def linear_search(lst, value):
    """ (list, object) -> intReturn the index of the last occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    2
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)-1
    """ 
    # The first index is included, the second is not, and the third is the

    # increment.
    for i in range(len(lst) -1, -1, -1):
        if lst[i] == value:
            return i
            return -1

# 3
# Sentinel


def linear_search(lst, value):
    """ (list, object) -> int
    
    Return the index of the last occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    2
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """ 
    # Add the sentinel at the beginning.
    lst.insert(0, value)
    
    i = len(lst) -1
    # Keep going until we find value.
    while lst[i] != value:
        i = i -1
        
    # Remove the sentinel.
    lst.pop(0)
    
    # If we reached the beginning of the list we didn't find value.
    if i == 0:
        return -1
    else:
        # When we inserted, we shifted everything one to the right. Subtract 1
        # to account for that.
        return i -1

if __name__ == '__main__': 
    import doctest
    print(doctest.testmod())

# Task 2
# For the new versions of linear search: if there are duplicate values, which do they find?
# - Should be with the highest index

# Task 5

import time
import random
def bubble_sort(lst):
    """ (list) -> NoneType
    
    Reorder the items in L from smallest to largest.
    
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bubble_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> L = []
    >>> bubble_sort(L)
    >>> L
    []
    >>> L = [1]
    >>> bubble_sort(L)
    >>> L
    [1]
    >>> L = [2, 1]
    >>> bubble_sort(L)
    >>> L
    [1, 2]
    >>> L = [1, 2]
    >>> bubble_sort(L)
    >>> L
    [1, 2]
    >>> L = [3, 3, 3]
    >>> bubble_sort(L)
    >>> L
    [3, 3, 3]
    >>> L = [-5, 3, 0, 3, -6, 2, 1, 1]
    >>> bubble_sort(L)
    >>> L
    [-6, -5, 0, 1, 1, 2, 3, 3]
    """

    # The end of the unsorted section.  The largest item will be placed here.
    end = len(lst) -1
    # Keep going until there are either 0 or 1 items to consider.
    # # (The 0 case is for the empty list.)
    while end > 0:
        # sweep through the list.
        for i in range(0, end):
            if lst[i] > lst[i + 1]:
                tmp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = tmp
                
        end = end -1

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]: 
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)

if __name__ == '__main__': 
    import doctest
    print(doctest.testmod())




# Task 7

# Modify the timing program to compare bubble sort with insertion and selection sort. Explain the results.



import time
import random
def bubble_sort(lst):
    """ (list) -> NoneType
    
    Reorder the items in L from smallest to largest.
    
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bubble_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> L = []
    >>> bubble_sort(L)
    >>> L
    []
    >>> L = [1]
    >>> bubble_sort(L)
    >>> L
    [1]
    >>> L = [2, 1]
    >>> bubble_sort(L)
    >>> L
    [1, 2]
    >>> L = [1, 2]
    >>> bubble_sort(L)
    >>> L
    [1, 2]
    >>> L = [3, 3, 3]
    >>> bubble_sort(L)
    >>> L
    [3, 3, 3]
    >>> L = [-5, 3, 0, 3, -6, 2, 1, 1]
    >>> bubble_sort(L)
    >>> L
    [-6, -5, 0, 1, 1, 2, 3, 3]
    """

    # The beginning of the unsorted section.  The largest item will be placed here

    beginning = 0
    
    # Keep going until there is only one item to consider.
    while beginning < len(lst):
        #sweep through the list.
        for i in range(len(lst) -1, beginning, -1):
            if lst[i] < lst[i -1]:
                tmp = lst[i -1]
                lst[i -1] = lst[i]
                lst[i] = tmp
                
        beginning = beginning + 1

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]: 
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)

if __name__ == '__main__': 
    import doctest
    print(doctest.testmod())
