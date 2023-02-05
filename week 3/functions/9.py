"""
9. Write a function that computes the volume of a sphere given its radius.
Formula: V = (4/3) *  pi * R^3
"""
from math import pi
def volume_by_radius(x):
    return (4 / 3) * pi * x ** 3

print(int(volume_by_radius(5)))