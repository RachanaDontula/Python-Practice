"""
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
from datetime import date
d1 = date(2019, 9, 11)
d2 = date(2019, 9, 18)
d3 = d2 - d1
print(d3.days)

"""
15. Write a Python program to get the volume of a sphere with radius 6.
volume of a sphere is (4/3)*pi*r*r*r
"""
pi = 3.14
r = int(input("Enter radius value: "))
volume = (4/3)*pi*r*r*r
print("The volume of sphere is: ", volume)

"""
16. Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference
"""
x = int(input("Enter an integer: "))
if x <= 17:
    print("The difference between the number and 17 is: ",(17 - x))
elif x > 17:
    print("The difference is absolute difference: ", 2*(abs(x-17)))

# 2nd type of code:
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return 2*(n - 17)


print(difference(52))
print(difference(16))