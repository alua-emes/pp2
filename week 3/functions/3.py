"""
3.Write a program to solve a classic puzzle:
We count 35 heads and 94 legs among the chickens
and rabbits in a farm. How many rabbits and
how many chickens do we have?
create function: solve(numheads, numlegs):
"""
def solve(numheads, numlegs):
    chichen = 0
    rabbit = 0

    rabbit = (numlegs - 2 * numheads)
    chicken = numheads - rabbit
    print("Number of chicken is {0} and Number of rabbit is {1}".format(int(chicken), int(rabbit)))

solve(35, 94)