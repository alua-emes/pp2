#Write a python program to convert snake case string to camel case string.
import re
text = input()
print(''.join(x.capitalize() or '_' for x in text.split('_')))
