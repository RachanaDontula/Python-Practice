"""29. Write a Python program to print out a set containing all the colors from color_list_1
which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}"""

color_list_1 = set(["1", "2", "3", "4"])
color_list_2 = set(["1", "5"])

print(color_list_1.difference(color_list_2))

"""30. Write a Python program that will accept the base and 
height of a triangle and compute the area."""

base = float(input("Enter the base of a triangle"))
height = float(input("Enter height of a triangle: "))
area = (1/2)*height*base
print("Area of a traingle is: ", area)

"""31. Write a Python program to compute the 
greatest common divisor (GCD) of two positive integers and 
32. Write a Python program to get the least common multiple (LCM) of two positive integers."""

import math
print(math.gcd(8,12))


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm


print(lcm(2, 4))
print(gcd(8, 12))
print(lcm(2, 4))
print(lcm(2, 4))

"""33. Write a Python program to sum of three given integers. 
However, if two values are equal sum will be zero."""


def sum_val(a, b, c):
    sum = a+b+c
    if (a == b) or (b == c) or (c == a):
        return 0
    else:
        return sum


print(sum_val(1, 2, 4))
print(sum_val(1, 1, 4))
print(sum_val(1, 96, 14))

"""34. Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20. """


def sum1_val(q, w):
    sum1 = q+w
    if sum1 in range(15, 20):
        return 20
    else:
        return sum1


print(sum1_val(1, 2))
print(sum1_val(12, 4))
print(sum1_val(1, 96))






