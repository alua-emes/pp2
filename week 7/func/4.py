'''Write a Python program that invoke square root function after specific milliseconds. 
Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is 158.42979517754858 '''

from time import sleep
import math

def invoker(n,t):
    x = math.sqrt(n)
    print("Square root of {} after {} milliseconds is {}".format(n, t, x))


n = int(input())
t = int(input())

print(invoker(n,t))