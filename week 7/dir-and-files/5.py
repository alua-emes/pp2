'''Write a Python program to write a list to a file. '''

items = [s for s in input().split()]
file = open('items.txt','w')
for x in items:
	file.write(x + "\n")
file.close()