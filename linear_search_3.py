def linear_search(lst, value):
	"""
	return the index of the first occurence of value in lst
	>>> linear_search([2,5,1,-3],5)
	"""

	lst.append(value)
	i= 0

	while lst[i] != value:
		i += 1

	lst.pop()

	if i == len(lst):
		return -1
	else:
		return i