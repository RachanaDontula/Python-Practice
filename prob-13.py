"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
x = int(input("Enter any integer: "))
if x in range(1,1000) and (1000,2000):
    if x in range(1,100):
        print("the number is within 1-100 of 1000")
    elif x > 100 & x <= 999:
        print("The number is not within 1-100 of 1000")
    elif x in range(1000, 1100):
        print("the number is in range of 1-100 of 2000")
else:
    print("the number is not in range of both first hundreds of both 1000 and 2000")


# 2nd possibility:


def near_thousand(n):
    return abs(1000 - n) <= 100 or abs(2000 - n) <= 100


print(near_thousand(566))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))