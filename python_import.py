#!/usr/bin/env python3

import math
type(math)
print(math.sqrt(9))
print(math.pi)
radius = 5 
print('area is', math.pi * radius ** 2)

import temperature
celsius = temperature.convert_to_celsius(90.1)
print(celsius)
print(temperature.above_freezing(celsius))

import panda_print
print('__name__ is ',__name__)

import main_example

import temperature_program

import baking

import hello

import calendar
tc= calendar.TextCalendar(firstweekday=0)
print(tc.prmonth(2016, 7))