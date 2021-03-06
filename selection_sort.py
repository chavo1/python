#!/usr/bin/env python3

def find_min(L,b):
	""" (list, int) -> int
	precondition: L[b:] is not empty
	return the index of the smallest value in L[b:]
	>>> find_min([3,-1,7,5], 0)
	1
	>>> find_min([3,-1,7,5], 1)
	1
	>>> find_min([3,-1,7,5], 2)
	3
	"""
	# the index of the smallest so far
	smallest = b
	i=b+1
	while i != len(L):
		if L[i] < L[smallest]:
			smallest = i
		i+=1
	return smallest

def selection_sort(L):
	""" (list) -> NoneType
	Reorder the items in L from smallest to largest
	>>> L = [3, 4, 7, -1, 2, 5]
	>>> selection_sort(L)
	>>> L
	[-1,2,3,4,5,7]
	"""
	i = 0
	while i != len(L):
		smallest = find_min(L,i)
		L[i], L[smallest] = L[smallest], L[i]
		i+=1
	return L

print (selection_sort([3, 4, 7, -1, 2, 5]))