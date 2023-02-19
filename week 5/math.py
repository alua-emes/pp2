# Python Math library

"""1. Write a Python program to convert degree to radian.

Input degree: 15
Output radian: 0.261904
"""
import math
n = int(input("Input degree: "))
print("Output radian: " + str(round(math.radians(n), 6)))

"""2. Write a Python program to calculate the area of a trapezoid.

Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
"""

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

area = ((a+b)/2)*h

print("Expected Output:" + str(area))
"""3. Write a Python program to calculate the area of regular polygon.

Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""

import math

s = float(input("Input number of sides: "))
l = float(input("Input the length of the side: "))

n = math.tan(math.radians((((s-2)*180)/(2*s))))

area = ((l**2)*n*s)/4

print("The area of the polygon is: " + str(round(area)))

"""4. Write a Python program to calculate the area of a parallelogram. 

Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0"""

b = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))

print("Expected Output: " + str(h*b))