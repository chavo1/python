#!/usr/bin/env python3
import temperature_program

def get_preheating_instructions(fahrenheit: float) -> str:
    """Return instruction for preheating the oven in fahrenheit degree and
    Celsius degree.

    >>> get_preheating_instructions(500)
    'Preheat oven to 500 degree F (260.0 degree C).'
    """
    cels = str(temperature_program.convert_to_celsius(fahrenheit))
    fahr = str(fahrenheit)
    return 'Preheat oven to ' + fahr + 'degrees F ('+ cels +' degrees C).'
    
fahr = float(input('Enter the baking temperature in degrees Fahrenheit: '))
print(get_preheating_instructions(fahr))
