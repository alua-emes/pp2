"""
7.Given a list of ints, return True if
the array contains a 3 next to a 3 somewhere.

    def has_33(nums):
        pass

    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
"""

def has_33(x):
    for i in range(len(x)-1):
        if x[i:i+2] == [3,3]:
            return True
    return False

numbers_str = input("Enter numbers and separate them by space: ")
numbers_list = []

for num_str in numbers_str.split():
    num_int = int(num_str)
    numbers_list.append(num_int)

print(has_33(numbers_list))
