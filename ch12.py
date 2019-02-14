#!/usr/bin/env python3

# Designing Algorithms /// top-down design

## What is smallest value? This code tells us just that - it is the data for past 10 years

counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
print (min(counts))

## If we want to know in which year the population bottomed out, we can use list.index to find the index of the smallest value:


counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
low = min(counts)
print (counts.index(low))

counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
print (counts.index(min(counts)))

# Lists have no method to find indices of the two smallest values?
# So we have to make an algorithm 

from typing import List, Tuple
def find_two_smallest1(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    # Find the index of the minimum and remove that item
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)
    # Find the index of the new minimum
    next_smallest = min(L)
    min2 = L.index(next_smallest)
    # Put smallest back into L
    L.insert(min1, smallest)
    # Fix min2 in case it was affected by the removal and reinsertion:
    if min1 <= min2: 
        min2 += 1
    
    return (min1, min2)


### Second way

from typing import List, Tuple
def find_two_smallest2(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    # Get a sorted copy of the list so that the two smallest items are at the # front
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]
    # Find the indices in the original list L
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)

    return (min1, min2)


### Third way
import time
import doctest
def find_two_smallest(L):
	""" (list of float) -> tuple of (int, int)
	Return a tuple of the indices of the two smallest values in list L
	>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
	(6, 7)
	"""
	# set min1 and min2 to the indices of the smallest and next smallest values at the beginning of L
	if L[0] < L[1]:
		min1, min2 = 0,1
	else:
		min1, min2 = 1,0
	# Examine each value in the list in order
	for i in range(2,len(L)):
		# Update these values when a new smaller value is found
		if L[i] < L[min1]:
			min2 = min1
			min1 = i
		elif L[i] <L[min2]:
			min2 = i
	return (min1,min2)

print (doctest.testmod())


# Exercises 
# 1
# A DNA sequence is a string made up of the letters A, T, G, and C. To find the complement of a DNA sequence,
# As are replaced by Ts, Ts by As, Gs by Cs, and Cs by Gs. For example, 
# the complement of AATTGCCGT is TTAACGGCA.

import doctest
def complement(sequence):
    """ (str) -> str
    Return the complement of sequence.
    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    """ 
    
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequence_complement = ''
    
    for char in sequence:
        sequence_complement = sequence_complement + complement_dict[char]
    
    return sequence_complement

print (doctest.testmod())

# 2
# In this exercise, you’ll develop a function that finds the minimum or 
# maximum value in a list, depending on the caller’s request.

import time
def min_or_max_index(L, flag):
    """ (list, bool) -> tuple of (object, int)
    Return the minimum or maximum item and its index from L, depending on
    whether flag is True or False.
    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], True)
    (1, 6)
    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], False)
    (6, 5)
    """ 
    index = 0
    current_value = L[0]
    if flag:
        for i in range(1, len(L)):
            if L[i] < current_value:
                index = i
                current_value = L[i]
    else:
        for i in range(1, len(L)):
            if L[i] > current_value:
                index = i
                current_value = L[i]        
        
    return (current_value, index)

print (doctest.testmod())

# 3
import doctest
def hopedale_average(filename):
    """ (str) -> float
    Return the average number of pelts produced per year for the data in 
    Hopedalefile named filename.
    """ 
    with open(filename, 'r') as hopedale_file:
        # Read the description line.
        hopedale_file.readline()
        
        # Keep reading comment lines until we read the first piece of 
        data = hopedale_file.readline().strip()
        while data.startswith('#'):
            data = hopedale_file.readline().strip()
            
        # Now we have the first piece of data append it to an empty list.
        pelts_list = []
        pelts_list.append(int(data))
        
        # Read the rest of the data.
        for data in hopedale_file:
            pelts_list.append(int(data.strip()))
            return sum(pelts_list) / len(pelts_list)

print (doctest.testmod())

# 4

# Write a set of doctests for the find-two-smallest functions. 
# Think about what kinds of data are interesting, long lists or short lists, 
# and what order the items are in. Here is one list to test with: [1, 2]. 
# What other interesting ones are there?

print (find_two_smallest([1, 2]))
print (find_two_smallest([3, 2]))
print (find_two_smallest([3, 3]))
print (find_two_smallest([3, 1, 3]))
print (find_two_smallest([1, 4, 2, 3, 4]))
print (find_two_smallest([4, 3, 1, 5, 6, 2]))
print (find_two_smallest([-2, 4, 3, 2, 5, 6, -1]))




# 6
def dutch_flag(flag):
  red_counter = 0
  index = 0
  while index != len(flag):
    if flag[index] == 'red':
      del flag[index]
      flag.insert(0, 'red')
      red_counter += 1
    elif flag[index] == 'green':
      del flag[index]
      flag.insert(red_counter, 'green')
    elif flag[index] == 'blue':
      del flag[index]
      flag.append('blue')
    if flag[index] == 'red':
      if index == 0 or flag[index-1] == 'red':
        index += 1
    elif flag[index] == 'green' and flag[index-1] != 'blue':
        index += 1
    elif flag[index] == 'blue':
      if index == len(flag) - 1 or flag[index] == 'blue':
        index += 1

def dutch_flag2(color_list):
  """ (list of str) -> list of str
  Return color_list rearranged so that 'red' strings come first, 'green'
  second,
  and 'blue' third.
  >>> color_list = ['red', 'green', 'blue', 'red', 'red', 'blue', 'red',
  'green']
  >>> dutch_flag(['red', 'green', 'blue', 'red', 'red', 'blue', 'red',
  'green'])
  >>> color_list
  ['red', 'red', 'red', 'red', 'green', 'green', 'blue', 'blue']
  """
  # The start of the green section.
  start_green = 0
  # The index of the first unexamined color.
  start_unknown = 0
  # The index of the last unexamined color.
  end_unknown = len(color_list) - 1
  while start_unknown <= end_unknown:
    # If it is red, swap it with the item to the right of the red section.
    if color_list[start_unknown] == 'red':
      color_list[start_green], color_list[start_unknown] \
      = color_list[start_unknown], color_list[start_green]
      start_green += 1
      start_unknown += 1
    # If it is green, leave it where it is.
    elif color_list[start_unknown] == 'green':
      start_unknown += 1
    # If it is blue, swap it with the item to the left of the blue section.
    else:
      color_list[start_unknown], color_list[end_unknown] \
      = color_list[end_unknown], color_list[start_unknown]
      end_unknown -= 1
def dutch_flag_runtime(function, list):
  """
  (function, list) -> float
  
  Returns the amount of milliseconds elapsed for the function to search through list.
  """
  time1 = time.perf_counter()
  function(list)
  time2 = time.perf_counter()
  return (abs(time2 -time1)*1000)
color_list = ['red', 'blue', 'green', 'green', 'red', 'blue', 'red', 'green']
color_list2 = ['red', 'blue', 'green', 'green', 'red', 'blue', 'red', 'green']
dutch_flag(color_list)
print(color_list)
dutch_flag2(color_list2)
print(color_list2)
print(dutch_flag_runtime(dutch_flag, color_list))
print(dutch_flag_runtime(dutch_flag2, color_list2))
print(dutch_flag_runtime(dutch_flag, color_list)/dutch_flag_runtime(dutch_flag2, color_list2))