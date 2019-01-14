#!/usr/bin/env python3

velocities = [0.0, 9.81, 19.62, 29.43]
print(('Metric:', velocities[0], 'm/sec;', 'Imperial:', velocities[0] * 3.28, 'ft/sec'))
print(('Metric:', velocities[1], 'm/sec;', 'Imperial:', velocities[1] * 3.28, 'ft/sec'))
print(('Metric:', velocities[2], 'm/sec; ', 'Imperial:', velocities[2] * 3.28, 'ft/sec'))
print(('Metric:', velocities[3], 'm/sec; ', 'Imperial:', velocities[3] * 3.28, 'ft/sec'))

# ***for loop***
#
#The general form of a for loop over a list is as follows: 
# for «variable» in «list»:
# «block»

for velocity in velocities:
    print(('Metric:', velocity, 'm/sec;', 'Imperial:', velocity * 3.28, 'ft/sec'))

# The variable is left holding its last value when the loop finishes:

speed = 2
for speed in velocities:
    print(('Metric:', speed, 'm/sec'))

# This is not a part of the loop

print(('Final:', speed))



# For example, we can loop over each character in a string, printing the uppercase letters:
country = 'United States of America'

for ch in country:
    if ch.isupper():
        print(ch)

# Python’s range type. You can use a loop to access each number in the sequence one at a time:


range(10)

for num in range(10):
    print((num))

    print(list(range(10)))
    print(list(range(3)))
    print(list(range(2)))
    print(list(range(1)))
    print(list(range(1, 10)))
    print(list(range(5, 10)))
    print(list(range(11, 5)))

# Here we produce a list of leap years in the first half of this century:
# positive
print(list(range(2000, 2050, 4)))
# negative
print(list(range(2050, 2000, -4)))
# It’s possible to loop over the sequence produced by a call on range.

total = 0
for i in range(1, 101): 
    total = total + i
    print(total)

# Processing Lists Using Indices

values = [4, 10, 3, 8, -6]

for num in values:
    num = num * 2

print(values)

values = [4, 10, 3, 8, -6]

for num in values:
    num = num * 2
    
print(num)
print(values)

# The correct approach is to loop over the indices of the list.

print(len(values))
print(list(range(5)))
print(list(range(len(values))))

# Rather than looping over values, you can iterate over its indices, which are produced by range(len(values)):

for i in range(len(values)):
    print(i)

# You can use each index to access the items in the list:

for i in range(len(values)):
    print(i, values[i])


for i in range(len(values)):
    values[i] = values[i] * 2
    print(values)

# Processing Parallel Lists Using Indices

metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]
for i in range(len(metals)):
    print(metals[i], weights[i])

# Nesting Loops in Loops

outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)

# After printing the header row, we use a nested loop to print each row of the table in turn, using tabs

def print_table(n: int) -> None:
    """Print the multiplication table for numbers 1 through n inclusive.
    >>> print_table(5)
        1   2   3   4   5
    1   1   2   3   4   5
    2   2   4   6   8   10
    3   3   6   9   12  15
    4   4   8   12  16  20
    5   5   10  15  20  25
    """
    # The numbers to include in the table.
    numbers = list(range(1, n + 1))

    # Print the header row.
    for i in numbers:
        print('\t' + str(i), end='')
# End the header row.
    print()

# Print each row number and the contents of each row.
    for i in numbers:
        print (i, end='') 
    for j in numbers:
        print('\t' + str(i * j), end='') 
    # End the current row.
        print()

# In addition to looping over lists of numbers, strings, and Booleans, we can also loop over lists of lists.

elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
for inner_list in elements:
    print(inner_list)
# To access each string in the inner lists, you can loop over the outer list and then over each inner list using a nested loop.
    for inner_list in elements:
        for item in inner_list:
            print(item)

# Looping Over Ragged Lists

info = [['Isaac Newton', 1643, 1727], ['Charles Darwin', 1809, 1882], ['Alan Turing', 1912, 1954, 'alan@bletchley.uk']]
for item in info:
    print(len(item))

drinking_times_by_day = [["9:02", "10:17", "13:52", "18:23", "21:31"], ["8:45", "12:44", "14:52", "22:17"], ["8:55", "11:11", "12:34", "13:46", "15:52", "17:08", "21:15"], ["9:15", "11:44", "16:28"], ["10:01", "13:33", "16:45", "19:00"],
["9:34", "11:16", "15:52", "20:37"], ["9:01", "12:24", "18:51", "23:13"]]

for day in drinking_times_by_day:
    for drinking_time in day: 
        print(drinking_time, end=' ')
    print()
# The inner loop iterates over the items of day, and the length of that list varies.


# While loop /// Looping Until a Condition Is Reached
#
# while «expression»: 
#      «block»

rabbits = 3
while rabbits > 0:
    print(rabbits)
    rabbits = rabbits - 1

# A simple exponential growth model, which is essentially a calculation of compound interest:

time = 0
population = 1000 # 1000 bacteria to start with
growth_rate = 0.21 # 21% growth per minute
while population < 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1

print("It took", time, "minutes for the bacteria to double.")
print("The final population was", round(population), "bacteria.")


# Infinite Loops


# Use multivalued assignment to set up controls

time, population, growth_rate = 0, 1000, 0.21

# Don't stop until we're exactly double the original size
#while population != 2000:
 #   population = population + growth_rate * population 
 #   print(round(population))
  #  time = time + 1
#print("It took", time, "minutes for the bacteria to double.")
#Whoops—since the population is never exactly two thousand bacteria, the loop never stops.


# Repetition Based on User Input
#  when the user types quit, the first condition, text == "quit", eval- uates to True. The print("...exiting program") 
# statement is executed, and then the break statement, which causes the loop to terminate.

text = ""
while text != "quit":
    text = input("Please enter a chemical formula (or 'quit' to exit): ") 
    if text == "quit":
        print("...exiting program") 
    elif text == "H2O":
        print("Water") 
    elif text == "NH3":
        print("Ammonia") 
    elif text == "CH4":
        print("Methane") 
    else:
        print("Unknown compound")

# Controlling Loops Using break and continue

s = 'C3H7'
digit_index = -1 # This will be -1 until we find a digit.
for i in range(len(s)):
    # If we haven't found a digit, and s[i] is a digit
    if digit_index == -1 and s[i].isdigit():
        digit_index = i
        break # This exits the loop.

print(digit_index)

# The continue Statement

s = 'C3H7'
total = 0 # The sum of the digits seen so far. 
count = 0 # The number of digits seen so far. 
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total = total + int(s[i])
    count = count + 1

print(total)
print(count)