#!/usr/bin/env python3

def find_min(L: list, b: int) -> int: 
    """Precondition: L[b:] is not empty.
    Return the index of the smallest value in L[b:].
    >>> find_min([3, -1, 7, 5], 0)
    1
    >>> find_min([3, -1, 7, 5], 1)
    1
    >>> find_min([3, -1, 7, 5], 2)
    3
    """
    smallest = b # The index of the smallest so far. 
    i=b+1
    while i != len(L):
        if L[i] < L[smallest]:
            # We found a smaller item at L[i].
            smallest = i 
        i=i+1
    return smallest

def selection_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    i=0
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i] 
        i=i+1

def insert(L: list, b: int) -> None: 
    """Precondition: L[0:b] is already sorted. 
    Insert L[b] where it belongs in L[0:b + 1].
    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    """
    # Find where to insert L[b] by searching backwards from L[b] 
    # # for a smaller item.
    i=b
    while i != 0 and L[i - 1] >= L[b]:
        i=i-1
    # Move L[b] to index i, shifting the following values to the right.
    value = L[b]
    del L[b] 
    L.insert(i, value)

def insertion_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    i=0
    while i != len(L):
        # Insert L[i] where it belongs in L[0:i+1].
        i=i+1

