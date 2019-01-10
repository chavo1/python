#!/usr/bin/env python3


# * Chapter * 
# * Storing Collections of Data Using Lists *

import calendar
tc= calendar.TextCalendar(firstweekday=0)
print(tc.prmonth(2019, 1,))

import datetime
print(datetime.datetime.now())

# using a list to keep track of the 14 days of whale counts. 

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
# A list is an object; like any other object, it can be assigned to a variable.
print (whales)
print (whales[0])
print (whales[1])
print (whales[12])
print (whales[13])
print (whales[-1])
print (whales[-2])
print (whales[-14])
third = whales[2]
print('Third day:', third)
# Lists can contain any type of data, including integers, strings, and even other lists.

krypton = ['Krypton', 'Kr', -157.2, -153.4]
print (krypton[0])
print (krypton[1])
print (krypton[2])

# A function to calculate the average of a list of floats
from typing import List
def average(L: list) -> float:
    """Return the average of the values in L.

    >>> average([1.4, 1.6, 1.8, 2.0])
    1.7
    """
# Assign a new value to a specific element of the list - contents of a list can be mutated.
nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
nobles[1] = 'neon'
print (nobles)

# Capitalize name
name = 'Darwin'
capitalized = name.upper()
print(capitalized)
print(name)

# functions in action working on a list of the half-lives of plutonium isotopes
half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
print(len(half_lives))
print(max(half_lives))
print(min(half_lives))
print(sum(half_lives))
print(sorted(half_lives))
print(half_lives)

# lists can be combined using the concatenation (+) operator:
original = ['H', 'He', 'Li']
final = original + ['Be']
print(final)

# multiply a list by an integer to get a new list containing the elements from the original list repeated that number of times

metals = ['Fe', 'Ni']
print(metals * 3)

# modify a list with del operator (which stands for delete). It can be used to remove an item from a list, as follows

metals = ['Fe', 'Ni']
del metals[0]
print(metals)

# The in operator can be applied to lists to check whether an object is in a list

nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
gas = input('Enter a gas: ')
# Enter a gas: argon
if gas in nobles:
    print('{} is noble.'.format(gas))
# argon is noble.

gas = input('Enter a gas: ')
# Enter a gas: nitrogen
if gas in nobles:
    print('{} is noble.'.format(gas))
# *empty*

# the in operator checks only for a single item.
print([1, 2] in [0, 1, 2, 3])


# Slicing List
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
print(celegans_phenotypes)
# This creates a new list consisting of only the four distinguishable markers, which are the first four items from the list that celegans_phenotypes refers to.
useful_markers = celegans_phenotypes[0:4]
print(useful_markers)
# The first index can be omitted if we want to slice from the beginning of the list, and the last index can be omitted if we want to slice to the end
useful_markers = celegans_phenotypes[:4]
print(useful_markers)
useful_markers = celegans_phenotypes[4:]
print(useful_markers)

# To create a copy of the entire list, omit both indices so that the “slice” runs from the start of the list to its end:
celegans_copy = celegans_phenotypes[:]
# An entire copy of the list
print(celegans_copy)
# A following will change the last value in the list
celegans_phenotypes[5] = 'Lvl'
print(celegans_phenotypes)

# Aliasing: What’s in a Name?
celegans_alias = celegans_phenotypes
celegans_phenotypes[5] = 'Lvl'
print(celegans_phenotypes)
print(celegans_alias)


# Mutable parameter
celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
def remove_last_item(L: list) -> list:
    """Return list L with the last item removed.
    Precondition: len(L) >= 0
    
    >>> remove_last_item([1, 3, 2, 4])
    [1, 3, 2]
    """
    del L[-1]
    return L
print(remove_last_item(celegans_markers))   
print(celegans_markers)

# Since remove_last_item modifies the list parameter, the modified list doesn’t actually need to be returned. You can remove the return statement:
celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
def remove_last_item(L: list) -> list:
    """Remove the last item from L.
    
    Precondition: len(L) >= 0
    
    >>> remove_last_item([1, 3, 2, 4])
    """
    del L[-1]
remove_last_item(celegans_markers)
print(celegans_markers)

from typing import List, Any
def remove_last_item(L: List[Any]) -> None:
    """Remove the last item from L.
    Precondition: len(L) >= 0

    >>> remove_last_item([1, 3, 2, 4])
    """
    del L[-1]

print(celegans_markers)


# List Methods

colors = ['red', 'orange', 'green']
colors.extend(['black', 'blue'])
print(colors)
# Append a color
colors.append('purple')
print(colors)
# Insert a color in a list
colors.insert(2, 'yellow')
print(colors)
# Remove a color
colors.remove('black')
print(colors)

#  many list methods return None rather than creating and returning a new list. As a result, lists sometimes seem to disappear:

colors = 'red orange yellow green blue purple'.split()
print(colors)

# In this example, colors.sort() did two things: it sorted the items in the list, and it returned the value None.
sorted_colors = colors.sort()
print(sorted_colors)
print(colors)

# Working with a List of Lists

life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
print(life[0])
print(life[1])
print(life[2])

# Since each of these items is also a list, we can index it again, just as we can chain together method calls or nest function calls:
print(life[1])
print(life[1][0])
print(life[1][1])

# We can also assign sublists to variables:
canada = life[0]
print(canada)
print(canada[0])
print(canada[1])

# As before, any change we make through the sublist reference will be seen when we access the main list, and vice versa:
canada[1] = 80.0
print(canada)
print(life)

# <---Exercises Exercises Exercises Exercises--->

# Variable kingdoms refers to the list ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']. Using kingdoms and either slicing or indexing with positive indices, write expressions that produce the following:

kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdoms[0])
print(kingdoms[5])
print(kingdoms[:3])
print(kingdoms[2:5])
print(kingdoms[4:])
del kingdoms[:6]
print(kingdoms)

#  Repeat the previous exercise using negative indices.
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdoms[-6])
print(kingdoms[-1])
print(kingdoms[-6:-3])
print(kingdoms[-4:-1])
print(kingdoms[-2:])
del kingdoms[:6]
print(kingdoms)

# Variable appointments refers to the list ['9:00', '10:30', '14:00', '15:00', '15:30']. An appointment is scheduled for 16:30, so '16:30' needs to be added to the list.

appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
appointments.append('16:30')
print(appointments)
appointments.remove('16:30')
print(appointments)
appointments += ['16:30']
print(appointments)

# Variable ids refers to the list [4353, 2314, 2956, 3382, 9362, 3900]. Using list methods, do the following:

ids = [4353, 2314, 2956, 3382, 9362, 3900]
ids.remove(3382)
print(ids)
print(ids[3])
ids.insert(4, 4499)
print(ids)
ids.extend([5566, 1830])
print(ids)
ids.insert(3, 3382)
ids.remove(5566)
ids.remove(1830)
ids.remove(4499)
print(ids)
sorted_ids = ids.sort()
print(sorted_ids)
print(ids)

# 5. In this exercise, you’ll create a list and then answer questions about that list.

#a. Assign a list that contains the atomic numbers of the six alkaline earth metals—beryllium (4), magnesium (12), calcium (20), strontium (38), barium (56), 
# and radium (88)—to a variable called alkaline_earth_metals.
#b. Which index contains radium’s atomic number? Write the answer in two ways, one using a positive index and one using a negative index.
#c. Which function tells you how many items there are in alkaline_earth_metals?
#d. Write code that returns the highest atomic number in alkaline_earth_metals.
#(Hint: Use one of the functions from Table 10, List Functions, on page 135.)

alkaline_earth_metals = ['4', '12', '20', '38', '56','88']

print(len(alkaline_earth_metals))
print(alkaline_earth_metals[5])
print(max(alkaline_earth_metals))
print(min(alkaline_earth_metals))

#6. In this exercise, you’ll create a list and then answer questions about that list.
#a. Create a list of temperatures in degrees Celsius with the values 25.2, 16.8, 31.4, 23.9, 28, 22.5, and 19.6, and assign it to a variable called temps.
#b. Using one of the list methods, sort temps in ascending order.
#c. Using slicing, create two new lists, cool_temps and warm_temps, which contain the temperatures below and above 20 degrees Celsius, respectively.
#d. Using list arithmetic, recombine cool_temps and warm_temps into a new list called temps_in_celsius.

temps = ['25.2', '16.8', '31.4', '23.9', '28', '22.5', '19.6']
temps.sort()
print(temps)

cool_temps = temps[0:2]
print(cool_temps)
warm_temps = temps[2:]
print(warm_temps)

temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)

# 7. Complete the examples in the docstring and then write the body of the following function:

def same_first_last(L: list) -> bool: 
    """Precondition: len(L) >= 2
    Return True if and only if first item of the list is the same as the
    last.
    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    >>> same_first_last([4.0, 4.5])
    False
    """
    return L[0] == L[-1]

print(same_first_last)

# 8. Complete the examples in the docstring and then write the body of the following function:

def is_longer(L1: list, L2: list) -> bool:
    """Return True if and only if the length of L1 is longer than the length of L2.
    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3]
    """