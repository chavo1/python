#!/usr/bin/env python3

import calendar
tc= calendar.TextCalendar(firstweekday=0)
print(tc.prmonth(2016, 7))


print('hello'.upper())
print('Happy Birthday!'.lower())
print('WeeeEEEEeeeEEEEeee'.swapcase())
print('ABC123'.isupper())
print('aeiouAEIOU'.count('a'))
print('hello'.endswith('o'))
print('hello'.startswith('H'))
print('Hello {0}'.format('Python'))
print('Hello {0}! Hello {1}!'.format('Python', 'World'))
#Variable season refers to 'summer'. Using string method format and variable season, write an expression that produces 'I love summer!'

season = '{} summer{}'
print(season.format('I love', '!'))

#Variables side1, side2, and side3 refer to 3, 4, and 5, respectively. Using string method format and those three variables, 
# write an expression that produces 'The sides have lengths 3, 4, and 5.'

side1 = '3'
side2 = '4'
side3 = '5'

print("The sides have lengths {}, {} and {}.".format(side1, side2, side3))

#Using string methods, write expressions that produce the following:
#
# a. copy of 'boolean' capitalized
# b. The first occurrence of '2' in 'CO2 H2O'
# c. The second occurrence of '2' in 'CO2 H2O'
# d. True if and only if 'Boolean' begins lowercase
# e. A copy of "MoNDaY" converted to lowercase and then capitalized
# f. A copy of " Monday" with the leading whitespace removed

print('boolean'.swapcase())
print('boolean'.islower())
print('MoNDaY'.lower())
print('MoNDaY'.upper())
print(' Monday'.strip())

# <<--Complete the examples in the docstring and then write the body of the following function:-->>
import doctest
def total_occurrences(s1: str, s2: str, ch: str) -> int:
    """Precondition: len(ch) == 1
	Return the total number of times that ch occurs in s1 and s2
	
	>>> total_occurrences('color', 'yellow', 'l')
	3
	>>> total_occurrences('red', 'blue','l')
	1
	>>> total_occurrences ('green', 'purple','b')
	0
	"""
    return s1.count(ch) + s2.count(ch)
    
print(total_occurrences('color', 'yellow', 'l'))
print(total_occurrences('red', 'blue','l'))
print(total_occurrences ('green', 'purple','b'))
print(doctest.testmod())
