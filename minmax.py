#!/usr/bin/env python3

# Task 5
import unittest
def find_min_max(values: list):
    """Print the minimum and maximum value from values.
    """

    min = None
    max = None
    # The first time the if-blocks in the for-loop are executed, 
    # the value is compared with None. Since such comparisons aren’t allowed in 
    # Python, the code throws an Error. To fix it, you’ll need to change the for-loop to this:
    
    # for value in values:
    #     if value > max:
    #         max = value
    #     if value < min:
    #         min = value
            
    for value in values:
        if max is None or value > max:
            max = value
        if min is None or value < min:
            min = value

    print('The minimum value is {0}'.format(min))
    print('The maximum value is {0}'.format(max))

unittest.main()