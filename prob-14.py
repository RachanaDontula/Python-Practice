"""
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return three times of their sum.
"""


def sum_thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

"""
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.
"""


def new_string(str):
    if len(str) > 2 and str[:2] == "Is":
        return str
    return "Is" + str


print(new_string("Array"))
print(new_string("Is Rachana"))

"""
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""


x = str(input("Enter a string: "))
n = int(input('Enter a number: '))
print("The copies of given string are: ", x * n)

# Using function:


def long_string(str1, d):
    result = ''
    for i in range(d):
        result = result + str1
    return result


print(long_string('Rachana', 5))