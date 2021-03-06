#!/usr/bin/env python3
def convert_to_celsius(fahrenheit: float) -> float:
    """Return the number of Celsius degrees equivalent to fahrenheit ... degrees.
    >>> convert_to_celsius(75)
    23.88888888888889
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0
def above_freezing(celsius: float) -> bool:
    return celsius > 0
