#Python iterators and generators

#1 Create a generator that generates the squares of numbers up to some number N.

n = int(input())
def gen(n):
    val = 0
    while val < n+1:
        yield val**2
        val = val + 1

for x in gen(n):
    print(x)
#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def gen2(n):
    var = 0
    while var < n:
        if var % 2 == 0:
            if var != n-2:
                string = str(var) + ","
                yield string
            else:
                yield var
        var = var + 1

n = int(input())
for x in gen2(n):
    print(x, end = " ")
#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def gen3(n):
    var = 1
    while var < n:
        if var % 3 == 0 and var % 4 == 0:
            yield var
        var = var + 1
def counter(n):
    for x in gen3(n):
        print(x)

n = int(input())
counter(n)

#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

arr = [int(x) for x in input().split()]
a, b = arr[0], arr[1]
squares = (x**2 for x in range(a, b))

for y in squares:
    print(y)
#5 Implement a generator that returns all numbers from (n) down to 0.

n = int(input())
gen5 = (x for x in range(n, -1, -1))
for y in gen5:
    print(y)