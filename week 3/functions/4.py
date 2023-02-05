"""
4.You are given list of numbers separated by spaces.
Write a function filter_prime which will take list
of numbers as an argument and returns only prime
numbers from the list.
"""
numbers_str = input("Enter numbers and separate them by space: ")
numbers_list = []

for num_str in numbers_str.split():
    num_int = int(num_str)
    numbers_list.append(num_int)

def filter_prime(x):
    prime_list = []
    for i in x:
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c = c + 1
        if c == 1:
            prime_list.append(i)
    print(prime_list)

filter_prime(numbers_list)