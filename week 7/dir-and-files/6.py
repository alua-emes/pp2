'''Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt'''

import string, os


if not os.path.exists("alph"):
   os.makedirs("alph")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)