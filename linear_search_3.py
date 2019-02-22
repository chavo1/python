#!/usr/bin/env python3

# Sentinel Search
def linear_search(lst, value):
	"""
	return the index of the first occurrence of value in lst
	>>> linear_search([2,5,1,-3],5)
	"""
	# Add the sentinel.
	lst.append(value)
	i= 0
	# Keep going until we find value.
	while lst[i] != value:
		i = i + 1
	# Remove the sentinel.
	lst.pop()
	# If we reached the end of the list we didn't find value.
	if i == len(lst):
		return -1
	else:
		return i