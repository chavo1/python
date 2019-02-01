#!/usr/bin/env python3

# Storing Data Using Other Collection Types

# Python has a type called set that allows us to store mutable collections of unordered, distinct items. 
# (Remember that a mutable object is one that you can modify.) Here we create a set containing the vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
print (vowels)

vowels = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
print (vowels)

# they contain the same items output True
print ({'a', 'e', 'i', 'o', 'u'} == {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'})

# Variable vowels refers to an object of type set:
print (type(vowels))
print (type({1, 2, 3}))
print (set())
print (type(set()))
print (set([2, 3, 2, 5]))

# In addition to lists, there are a couple of other types that can be used as arguments to function set. One is a set:

vowels = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
print (vowels)
print (set(vowels))
print (set({5, 3, 1}))
print (set(range(5)))


vowels = {'a', 'e', 'i', 'o', 'u'}
print (vowels)

vowels.add('y')
print (vowels)
########
# In the following code, we show all of these methods in action:
########

ten = set(range(10))
lows = {0, 1, 2, 3, 4}
odds = {1, 3, 5, 7, 9}
lows.add(9)
print (lows)
print (lows.difference(odds))
print (lows.issubset(ten))
print (lows.issuperset(odds))
lows.remove(0)
print (lows)
print (lows.symmetric_difference(odds))
print (lows.union(odds))
lows.clear()
print (lows)


###########
# Set operations in action:
###########

lows = set([0, 1, 2, 3, 4])
odds = set([1, 3, 5, 7, 9])

print (lows - odds)  # Equivalent to lows.difference(odds)
print (lows & odds)  # Equivalent to lows.intersection(odds)
print (lows <= odds) # Equivalent to lows.issubset(odds)
print (lows >= odds) # Equivalent to lows.issuperset(odds)
print (lows | odds)  # Equivalent to lows.union(odds)
print (lows ^ odds)  # Equivalent to lows.symmetric_difference(odds)

# The following program reads each line of the file, strips off the leading and
# trailing whitespace, and adds the species on that line to the set. Notice the 
# type annotation specifying that the function returns a set of strings:

from typing import Set, TextIO
from io import StringIO
def observe_birds(observations_file: TextIO) -> Set[str]:
    """Return a set of the bird species listed in observations_file, which has one bird species per line.
    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> birds = observe_birds(infile)
    >>> 'bird 1' in birds
    True
    >>> 'bird 2' in birds
    True
    >>> len(birds) == 2
    True
    """
    birds_observed = set()
    for line in observations_file:
        bird = line.strip()
        birds_observed.add(bird)
    return birds_observed

if __name__ == '__main__': 
    import doctest
    doctest.testmod()
    with open('file_examples/observations.txt') as observations_file:
        print(observe_birds(observations_file))
    
# Set Contents Must Be Immutable

# >>> S = set()
# >>> L = [1, 2, 3]
# >>> S.add(L)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'set'

# Storing Data Using Tuples
rock = 'anthracite'
print (rock[9])
print (rock[0:3])
print (rock[-5:])
