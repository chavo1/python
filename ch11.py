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

# Storing Data Using Tuples //// A tuple is a collection which is ordered and unchangeable. 
# In Python tuples are written with round brackets.
rock = 'anthracite'
print (rock[9])
print (rock[0:3])
print (rock[-5:])
for character in rock[:5]:
    print(character)


 # Tuples are written using parentheses instead of brackets; 
 # like strings and lists, they can be subscript- ed, sliced, and looped over:

bases = ('A', 'C', 'G', 'T')
for base in bases:
     print(base)

print ((8))
print (type((8)))
print ((8,))
print ((5 + 3))
print ((5 + 3,))

# Unlike lists, once a tuple is created, it cannot be mutated:
# However, the objects inside tuples can still be mutated:

life = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
life[0][1] = 80.0
print (life)

# We’ll build the same tuple as in the previous example,
#  but we’ll do it in steps. First let’s create three lists:

canada = ['Canada', 76.5]
usa = ['United States', 75.5]
mexico = ['Mexico', 72.0]
life = (canada, usa, mexico)
mexico = ['Mexico', 72.5]
print (life)

# And because variable canada also refers to that list, it sees the mutation:

life[0][1] = 80.0
print (canada)

# Assigning to Multiple Variables Using Tuples

(x, y) = (10, 20)
print (x)
print (y)

# Python uses the comma as a tuple constructor, so we can leave off the parentheses:

print (10, 20)
x, y = 10, 20
print (x)
print (y)

# In fact, multiple assignment will work with lists and sets as well. 
# Python will happily pull apart information out of any collection:

[[w, x], [[y], z]] = [{10, 20}, [(30,), 40]]
print (w)
print (x)
print (y)
print (z)


# One of the most common uses of multiple assignment is to swap the values of two variables:

s1 = 'first'
s2 = 'second'
s1, s2 = s2, s1
print (s1)
print (s2)


# The following code uses a Boolean variable, found. Once a species is read from the file, 
# found is assigned False. The program then iterates over the list, looking for that species 
# at index 0 of one of the inner lists. If the species occurs in an inner list, found is assigned True.

from typing import TextIO, List, Any
from io import StringIO

def count_birds(observations_file: TextIO) -> List[List[Any]]:
    """Return a set of the bird species listed in observations_file, which has one bird species per line.
    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> count_birds(infile)
    [['bird 1', 2], ['bird 2', 1]]
    """
    bird_counts = []
    for line in observations_file:
        bird = line.strip()
        found = False
        # Find bird in the list of bird counts.
        for entry in bird_counts:
            if entry[0] == bird:
                entry[1] = entry[1] + 1
                found = True
        if not found: bird_counts.append([bird, 1])
    return bird_counts

if __name__ == '__main__':
    with open('file_examples/observations.txt') as observations_file:
        bird_counts = count_birds(observations_file)
        # Print each bird and the number of times it was seen
        for entry in bird_counts:
            print(entry[0], entry[1])

# Like the elements in sets, keys must be immutable (though the values associated with them don’t have to be). 
# putting key/value pairs inside braces (each key is followed by a colon and then by its value):

bird_to_observations = {'canada goose': 3, 'northern fulmar': 1}
print (bird_to_observations)

# To get the value associated with a key, we put the key in square brackets, much like indexing into a list:

print (bird_to_observations['northern fulmar'])
print (bird_to_observations['canada goose'])
 
# As with sets, dictionaries are unordered:

dict1 = {'canada goose': 3, 'northern fulmar': 1}
dict2 = {'northern fulmar': 1, 'canada goose': 3}
print (dict1 == dict2)


# Updating and Checking Membership

bird_to_observations = {}

# Add a new key/value pair, 'snow goose': 33
bird_to_observations['snow goose'] = 33

# Add a new key/value pair, 'eagle': 999.
bird_to_observations['eagle'] = 999

print (bird_to_observations)

# Change the value associated with key 'eagle' to 9.
bird_to_observations['eagle'] = 9
print (bird_to_observations)


# To remove an entry from a dictionary, use del d[k], where d is the dictionary 
# and k is the key being removed. Only entries that are present can be removed; 
# trying to remove one that isn’t there results in an error:

bird_to_observations = {'snow goose': 33, 'eagle': 9}
del bird_to_observations['snow goose']

print (bird_to_observations)

# To test whether a key is in a dictionary, we can use the in operator:

bird_to_observations = {'eagle': 999, 'snow goose': 33}
print ('eagle' in bird_to_observations)

if 'eagle' in bird_to_observations:
    print('eagles have been seen')

del bird_to_observations['eagle']
print ('eagle' in bird_to_observations)

if 'eagle' in bird_to_observations:
    print('eagles have been seen')

#Looping Over Dictionaries

bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71,
    'snow goose': 63, 'northern fulmar': 1}

for bird in bird_to_observations:
    print(bird, bird_to_observations[bird])

# Dictionary Operations

scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,
 'Turing' : 1912}

print (scientist_to_birthdate.keys())

print (scientist_to_birthdate.values())

