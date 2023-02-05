"""
1.A recipe you are reading states how many
grams you need for the ingredient. Unfortunately,
your store only sells items in ounces. Create
a function to convert grams to ounces.
ounces = 28.3495231 * grams
"""
def my_function(x):
    return 28.3495231 * x

grams = 10
ounces = my_function(grams)
print (ounces)