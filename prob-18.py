"""35. Write a Python program that will return true
if the two given integer values are equal or their sum or difference is 5."""


def sum_val(x, y):
    sum = x + y
    diff = abs(x - y)
    if (x == y) or (sum == 5) or (diff == 5):
        return True
    else:
        return sum


print(sum_val(1, 1))
print(sum_val(1, 4))
print(sum_val(1, 6))
print(sum_val(1, 10))

"""36. Write a Python program to add two objects 
if both objects are an integer type."""


def add_obj(a, b):
    sum1 = a + b
    if isinstance(a, int) and isinstance(b, int):
        return sum1
    else:
        return None


print(add_obj(1.1, 2))
print(add_obj(1, 2))

"""37. Write a Python program to display your details like 
name, age, address in three different lines."""


name = "Rachana"
age = 25
address = "Sea taste garden"
print("Name: {}\nAge: {}\nAdress: {}".format(name, age, address))

"""38. Write a Python program to solve (x + y) * (x + y). Go to the editor
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49"""


def square_num(u, v):
    square = (u + v) * (u + v)
    return square


print(square_num(4, 3))
print(square_num(41, 25))

# to get particular format, use .format
q, w = 4, 3
square1 = (q + w) * (q + w)
print("({} + {}) ^ 2 = {}".format(q, w, square1))

"""39. Write a Python program to compute the future value of a specified principal amount, 
rate of interest, and a number of years. Go to the editor
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79"""


PA = 10000
R = 3.5
Y = 7
# Future value =>  FV A = PA*((1+(0.01*R)) ** Y)
FV = PA*((1+(0.01*R)) ** Y)
print(round(FV, 2))

"""40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
Distance between points is: d(P, Q) = √ (x2 − x1)2 + (y2 − y1)2"""

import math
P = (4, 0)
Q = (6, 6)
D = math.sqrt(((Q[0] - P[0]) ** 2) + ((Q[1] - P[1]) ** 2))
print(D)



