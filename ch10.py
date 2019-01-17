#!/usr/bin/env python3

# Reading and Writing Files

# To check the current directory
import os
print(os.getcwd())

# To look for file in different directory

file = open('file_examples/file_example.txt', 'r')
contents = file.read()
file.close()
print(contents)

# Another way look for file in different directory

with open('file_examples/file_example.txt', 'r') as file:
    contents = file.read()
print(contents)

# Reads ten characters and then the rest of the file:
# Method call example_file.read(10) moves the file cursor, 
# so the next call, exam- ple_file.read(), reads everything from character 11 to the end of the file.

with open('file_examples/file_example.txt', 'r') as example_file:
    first_ten_chars = example_file.read(10)
    the_rest = example_file.read()

print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)

# This example reads the contents of a file into a list of strings and then prints that list:

with open('file_examples/file_example.txt', 'r') as example_file:
    lines = example_file.readlines()
print(lines)

with open('file_examples/planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()
print(planets)

for planet in reversed(planets):
    print(planet.strip())

# The “For Line in File” Technique

with open('file_examples/planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line))

#  whitespace characters (spaces, tabs, and newlines) stripped away:

with open('file_examples/planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line.strip()))

# The Readline Technique

with open('file_examples/hopedale.txt', 'r') as hopedale_file: 
    # Read and skip the description line.
    hopedale_file.readline()
    # Keep reading and skipping comment lines until we read the first piece # of data.

    data = hopedale_file.readline().strip()
    while data.startswith('#'):
        data = hopedale_file.readline().strip()
        # Now we have the first piece of data. Accumulate the total number of # pelts.

    total_pelts = int(data)

    # Read the rest of the data.
    for data in hopedale_file:
        total_pelts = total_pelts + int(data.strip())
            
print("Total number of pelts:", total_pelts)

# Each call on the function readline moves the file cursor to the beginning of the next line.


# Here is a program that prints the data from that file, preserving the whitespace:


with open('file_examples/hopedale.txt', 'r') as hopedale_file: 
    # Read and skip the description line.
    hopedale_file.readline()
    # Keep reading and skipping comment lines until we read the first piece # of data.

    data = hopedale_file.readline().rstrip()
    while data.startswith('#'):
        data = hopedale_file.readline().rstrip()
        
        # Now we have the first piece of data.
    print(data)

    # Read the rest of the data.
    for data in hopedale_file:
        print(data.rstrip())

# Files over the Internet

import urllib.request
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)

# Writing Files

with open('file_examples/topics.txt', 'w') as output_file:
    output_file.write('Computer Science')

with open('file_examples/topics.txt', 'a') as output_file:
    output_file.write('\nSoftware Engineering')

# The next example, in a file called total.py, is more complex, and it involves both reading from and writing to a file. 
# Notice that it uses typing.
# TextIO as the type annotation for an open file. “IO” is short for “Input/Output.” 
# Our input file contains two numbers per line separated by a space. The output file will contain three numbers per line: 
# the two from the input file followed by their sum (all separated by spaces).

from typing import TextIO
from io import StringIO

def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None: 
    """Read the data from input_file, which contains two floats per line
    separated by a space. output_file for writing and, for each line in
    input_file, write a line to output_file that contains the two floats from
    the corresponding line of input_file plus a space and the sum of the two
    floats.
    """
    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)

if __name__ == '__main__':
    with open('file_examples/number_pairs.txt', 'r') as input_file, \
            open('file_examples/number_pair_sums.txt', 'w') as output_file:
        sum_number_pairs(input_file, output_file)


# Writing Example Calls Using StringIO
# Here, we create a StringIO object containing the same information as file num- ber_pairs.txt, and read the first line:

from io import StringIO
input_string = '1.3 3.4\n2 4.2\n-1 1\n'
infile = StringIO(input_string)
print(infile.readline())

# We can also write to StringIO objects as if they were files, and retrieve their contents as a string using method getvalue:

from io import StringIO
outfile = StringIO()
print(outfile.write('1.3 3.4 4.7\n'))
print(outfile.write('2 4.2 6.2\n'))
print(outfile.write('-1 1 0.0\n'))
print(outfile.getvalue())




from typing import TextIO
from io import StringIO

def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
    """Read the data from input_file, which contains two floats per line
    separated by a space. output_file for writing and, for each line in
    input_file, write a line to output_file that contains the two floats from
    the corresponding line of input_file plus a space and the sum of the two
    floats.
    >>> infile = StringIO('1.3 3.4\\n2 4.2\\n-1 1\\n')
    >>> outfile = StringIO()
    >>> sum_number_pairs(infile, outfile)
    >>> outfile.getvalue()
    '1.3 3.4 4.7\\n2 4.2 6.2\\n-1 1 0.0\\n'
    """
    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)
if __name__ == '__main__':
    with open('file_examples/number_pairs.txt', 'r') as input_file, \
            open('file_examples/number_pair_sums.txt', 'w') as output_file:
        sum_number_pairs(input_file, output_file)






# Writing Algorithms That Use the File-Reading Techniques

from typing import TextIO
from io import StringIO

def skip_header(reader: TextIO) -> str:
    """Skip the header in reader and return the first real piece of data.
    >>> infile = StringIO('Example\\n# Comment\\n# Comment\\nData line\\n')
    >>> skip_header(infile)
    'Data line\\n'
    """
    # Read the description line
    line = reader.readline()
    # Find the first non-comment line
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()
    # Now line contains the first real piece of data
    return line

def process_file(reader: TextIO) -> None:
    """Read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with '#', then a
    sequence of data.
    >>> infile = StringIO('Example\\n# Comment\\nLine 1\\nLine 2\\n')
    >>> process_file(infile)
    Line 1
    Line 2
    """
    # Find and print the first piece of data
    line = skip_header(reader).strip()
    print(line)
    # Read the rest of the data
    for line in reader:
        line = line.strip()
        print(line)
if __name__ == '__main__':
    with open('file_examples/hopedale.txt', 'r') as input_file:
        process_file(input_file)

# This program processes the Hopedale data set to find the smallest number of fox pelts produced in any year.
# As we progress through the file, we keep the smallest value seen so far in a variable called smallest.
# That variable is initially set to the value on the first line, since it’s the smallest (and only) value seen so far:

from typing import TextIO
import time_series

def smallest_value(reader: TextIO) -> int:
    """Read and process reader and return the smallest value after the
    time_series header.
    >>> infile = StringIO('Example\\n1\\n2\\n3\\n')
    >>> smallest_value(infile)
    1
    >>> infile = StringIO('Example\\n3\\n1\\n2\\n')
    >>> smallest_value(infile)
    1
    """
    line = time_series.skip_header(reader).strip()
    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = int(line)
    for line in reader:
        value = int(line.strip())
        # If we find a smaller value, remember it.
        if value < smallest:
            smallest = value
    return smallest

if __name__ == '__main__':
    with open('file_examples/hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))


# To fix our code, we must add a check inside the loop that processes a line only if it contains a real value.
# We will assume that the first value is never a hyphen because in the TSDL data sets, missing entries are always marked with hyphens.
# So we just need to check for that before trying to convert the string we have read to an integer:


from typing import TextIO
from io import StringIO
import time_series

def smallest_value_skip(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header.
    Return the smallest value after the header. Skip missing values, which
    are indicated with a hyphen.
    >>> infile = StringIO('Example\\n1\\n-\\n3\\n')
    >>> smallest_value_skip(infile)
    1
    """
    line = time_series.skip_header(reader).strip()
    # Now line contains the first data value; this is also the smallest value # found so far, because it is the only one we have seen.
    smallest = int(line)
    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)
    
    return smallest

if __name__ == '__main__':
    with open('file_examples/hebron.txt', 'r') as input_file:
        print("This is smallest value: ", smallest_value_skip(input_file))