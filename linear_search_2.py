#!/usr/bin/env python3

# for Loop Version of Linear Search
def linear_search(lst, value):
	"""Return the index of the first occurrence of value in lst, or return
	 -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
	-1
    >>> linear_search([], 5)
    -1
    """
	for i in range(len(lst)):
		if lst[i] == value:
			return i
	return -1