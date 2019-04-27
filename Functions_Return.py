# Functions_Return.py
# Matt
# Aprril 1 2019

# Use the return values of Functions_Return
# Add two numbers together and return the result

import math
def sum_two_numbers(a,b):
    result = a + b 
    return result
def volume_cylinder(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

volume_of_can = volume_cylinder(2.5, 5)
volume_of_sixpack = volume_cylinder(2.5, 5) * 6
print(volume_of_can)
print(volume_of_sixpack)
answer = sum_two_numbers(1,2)
print(answer)