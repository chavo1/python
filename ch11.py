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
print (scientist_to_birthdate.items())
print (scientist_to_birthdate.get('Newton'))
print (scientist_to_birthdate.get('Curie', 1867))
print (scientist_to_birthdate)

researcher_to_birthdate = {'Curie' : 1867, 'Hopper' : 1906, 
'Franklin' : 1920}
scientist_to_birthdate.update(researcher_to_birthdate)
print (scientist_to_birthdate)
print (researcher_to_birthdate)
print (researcher_to_birthdate.clear())
print (researcher_to_birthdate)
###############
# loop over the scientists and their birth years:
###############
scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809, 'Turing' : 1912}
for scientist, birthdate in scientist_to_birthdate.items(): 
    print(scientist, 'was born in', birthdate)

# Each time we read an observation from a file, 
# we check to see whether we have encountered that bird before—that is,
#  whether the bird is already a key in our dictionary.

from typing import TextIO, Dict
from io import StringIO
def count_birds(observations_file: TextIO) -> Dict[str, int]:
    """Return a set of the bird species listed in observations_file, which has
    one bird species per line.
    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> count_birds(infile)
    {'bird 1': 2, 'bird 2': 1}
    """
    bird_to_observations = {}
    for line in observations_file:
        bird = line.strip()
        if bird in bird_to_observations:
            bird_to_observations[bird] = bird_to_observations[bird] + 1
        else:
            bird_to_observations[bird] = 1

    return bird_to_observations
    
if __name__ == '__main__':
    with open('file_examples/observations.txt') as observations_file:
        bird_to_observations = count_birds(observations_file)
        for bird, observations in bird_to_observations.items():
            print(bird, observations)

# The function body can be shortened by using the method dict.get, which saves three lines.

def count_birds(observations_file: TextIO) -> Dict[str, int]:
    """Return a set of the bird species listed in observations_file, which has one bird species per line.
    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> count_birds(infile)
    {'bird 1': 2, 'bird 2': 1}
    """
    bird_to_observations = {}
    for line in observations_file:
        bird = line.strip()
        bird_to_observations[bird] = bird_to_observations.get(bird, 0) + 1

    return bird_to_observations

if __name__ == '__main__':
    with open('file_examples/observations.txt') as observations_file:
        bird_to_observations = count_birds(observations_file)
        for bird, observations in bird_to_observations.items():
            print(bird, observations)

# Inverting a Dictionary // You might want to print the birds in another order

print (bird_to_observations)

# Invert the dictionary
observations_to_birds_list = {}
for bird, observations in bird_to_observations.items():
    if observations in observations_to_birds_list:
        observations_to_birds_list[observations].append(bird)
    else:
        observations_to_birds_list[observations] = [bird]

print (observations_to_birds_list)
    

# Print the inverted dictionary

observations_sorted = sorted(observations_to_birds_list.keys())

for observations in observations_sorted:
    print(observations, ':', end=" ")
    for bird in observations_to_birds_list[observations]:
        print(' ', bird, end=" ")
        print()

# Using the in Operator on Tuples, Sets, and Dictionaries

odds = set([1, 3, 5, 7, 9])
print (9 in odds)
print (8 in odds)
print ('9' in odds)
evens = (0, 2, 4, 6, 8)
print (4 in evens)
print (11 in evens)

# When used on a dictionary, in checks whether a value is a key in the dictionary:

bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71, 'snow goose': 63, 'northern fulmar': 1}

print ('snow goose' in bird_to_observations)
print (183 in bird_to_observations)

 # Exercises Chapter 11

# Task 1
# Write a function called find_dups that takes a list of integers as its input argu-ment 
# and returns a set of those integers occurring two or more times in the list.

def find_dups(L):
     """ (list) -> set
     
     Return the number of duplicates numbers from L.
     >>> find_dups([1, 1, 2, 3, 4, 2]){1, 2}
     >>> find_dups([1, 2, 3, 4])
     set()
     """ 
     
     elem_set = set()
     dups_set = set()
     
     for entry in L:
         len_initial = len(elem_set)
         elem_set.add(entry)
         len_after = len(elem_set)
         if len_initial == len_after:
             dups_set.add(entry)

     return(dups_set)


# Task2
# Write the bodies of the new versions of functions read_molecule and read_all_molecules from Creating New Type Annotations, on page 224.

def mating_pairs(males, females):
    """ (set, set) -> set of tupleReturn a set of tuples where each tuple contains a male from males and a 
    female from females.
    
    >>> mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 'Chen'})
    {('Cari', 'Chen'), ('Beatrice', 'Bob'), ('Anne', 'Ali')}
    """ 
    pairs = set()
    num_gerbils = len(males)
    
    for i in range(num_gerbils):
        
        male = males.pop()
        female = females.pop()
        pairs.add((male, female),)
        
    return pairs

print (mating_pairs)

# Task3
#Python’s set objects have a method called pop that removes and returns an arbitrary 
# element from the set. If the set gerbils contains five cuddly little ani- mals, for example, 
# calling gerbils.pop() five times will return those animals one by one, leaving the set empty at the end. 
# Use this to write a function called mating_pairs that takes two equal-sized sets called males and females as 
# input and returns a set of pairs; each pair must be a tuple containing one male and one female. 
# (The elements of males and females may be strings containing gerbil names or gerbil ID numbers—your function must work with both.)
# 

def get_authors(filenames):
    """ (list of str) -> set of str
    Return a list of the authors in PDB files names appear in filenames.
    """ 
    authors = set()
    
    for filename in filenames:
        pdb_file = open(filename)
        
        for line in pdb_file:
            if line.lower().startswith('author'):
                author = line[6:].strip()
                authors.add(author)

    return authors

# Task4
# The PDB file format is often used to store information about molecules. 
# A PDB file may contain zero or more lines that begin with the word AUTHOR 
# (which may be in uppercase, lowercase, or mixed case), followed by spaces or tabs, 
# followed by the name of the person who created the file. Write a function that takes a 
# list of filenames as an input argument and returns the set of all author names found in those files.

def count_values(dictionary):
    """ (dict) -> intReturn the number of unique values in dictionary.
    >>> count_values({'red': 1, 'green': 2, 'blue': 2})2
    """ 
    
    return len(set(dictionary.values()))

# Task5
# The keys in a dictionary are guaranteed to be unique, but the values are not. 
# Write a function called count_values that takes a single dictionary as an argument report erratum • 
# discuss and returns the number of distinct values it contains. Given the input {'red': 1, 'green': 1, 'blue': 2}, 
# for example, it should return 2.

def least_likely(particle_to_probability):
    """ (dict of {str: float}) -> str
    Return the particle from particle_to_probability with the lowest 
    probablity.
    >>> least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon':
    0.07})
    'meson'
    """ 
    smallest = 1
    name = ''
    
    for particle in particle_to_probability:
        probability = particle_to_probability[particle]
        if probability < smallest:
                smallest = probability
                name = particle

    return particle

# Task 6

def count_duplicates(dictionary):
    """ (dic) -> intReturn the number of duplicate values in dictionary.
    >>> count_duplicates({'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3})2
    """ 
    duplicates = 0
    values = list(dictionary.values())
    for item in values:
    # if an item appears at least 2 times, it is a duplicate
        if values.count(item) >= 2:
            duplicates = duplicates + 1
            # remove that item from the list
            num_occurrences = values.count(item) 
            for i in range(num_occurrences):
                values.remove(item)

    return duplicates

# Task 7

def is_balanced(color_to_factor):
    """ (dict of {str: float}) -> boolReturn True if and only if color_to_factor represents a balanced color.
    >>> is_balanced({'R': 0.5, 'G': 0.4, 'B': 0.7})
    False
    >>> is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})
    True
    """ 
    values = list(color_to_factor.values())
    total = sum(values)
    return total == 1.0

# Task 8

def dict_interest(dict1, dict2):
    """ (dict, dict) -> dictReturn a new dictionary that contains only the key/value pairs that occur
    in both dict1 and dict2.
    >>> dict_interest({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'd': 2, 'b': 2})
    {'a': 1, 'b': 2}
    """ 
    intersection = {}
    for (key, value) in dict1.items():
        if key in dict2 and value == dict2[key]:
            intersection[key] = value

    return intersection

# Task 9

def db_headings(dict_of_dict):
    """ (dict of dict) -> setReturn a set of the keys in the inner dictionaries in dict_of_dict.
    >>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}}){1, 2, 3}
    """ 
    inner_keys = set()
    for key in dict_of_dict:
        for inner_key in dict_of_dict[key]:
            inner_keys.add(inner_key)

    return inner_keys

# Task 11

def db_consistent(dict_of_dict):
    """ (dict of dict) -> set
    Return whether all inner dictionaries in dict_of_dict contain the same 
    keys.
    >>> db_consistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    False
    >>> db_consistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 1: 'd'}})
    True
    """ 
    inner_keys_list = []
    # Build a list of list of keys
    for key in dict_of_dict:
        inner_keys = list(dict_of_dict[key].keys())
        inner_keys.sort()
        inner_keys_list.append(inner_keys)
        for i in range(1, len(inner_keys_list)):
        # If the number of keys is different.
            if len(inner_keys_list[0]) != len(inner_keys_list[i]):
                return False
                # If the keys don't match.
                for j in range(len(inner_keys_list[0])):
                    if inner_keys_list[0][j] != inner_keys_list[i][j]:
                        return False

    return True


# Task 12
# a
def sparse_add(vector1, vector2):
    """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})
    Return the sum of sparse vectors vector1 and vector2.
    >>> sparse_add({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
    {1: 3, 2: 4, 3: 9, 5: 6}
    """ 
    sum_vector = vector1.copy()
    for key in vector2:
        if key in sum_vector:
            sum_vector[key] = sum_vector[key] + vector2[key]
        else:sum_vector[key] = vector2[key]
            
    return sum_vector
# b

def sparse_dot(vector1, vector2):
    """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})
    Return the dot product of sparse vectors vector1 and vector2.
    >>> sparse_dot({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})20
    """ 
    dot = 0
    for key1 in vector1:
        if key1 in vector2:
            dot = dot + vector1[key1] * vector2[key1]
            
    return dot
