""""
2.Read in a Fahrenheit temperature.
Calculate and display the equivalent
centigrade temperature. The following
formula is used for the conversion:
C = (5 / 9) * (F – 32)
"""

def my_function(f):
    return (5 / 9) * (f - 32)

fahr = 15
cent = my_function(fahr)
print(cent)
#another way of formatting the output
#print "{0} fahrenheit is {1} centigrade".format(f, c)