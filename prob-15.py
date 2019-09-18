"""
21. Write a Python program to find whether a given number (accept from the user) is even or odd,
print out an appropriate message to the user.
"""

x = int(input("Enter the number: "))
if (x % 2) == 0:
    print("The number is even")
else:
    print("The number is odd")


"""
22. Write a Python program to count the number 4 in a given list
"""


def list_numbers(nums):
    count1 = 0
    for j in nums:
        if j == 4:
            count1 = count1+1

    print(count1)


list_numbers([1,2,3,4,5,7,4,4,5])
list_numbers([5,1,4,15,14,4,9])
list_numbers([1,2,3,5,6,7,6])

"""
23. Write a Python program to get the n (non-negative integer) 
copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2.
"""

a = str(input("Enter a string: "))
b = int(input("Enter number of times the letters should be repeated: "))
print("Repeated letters are: ", a[:2] * b)
if len(a) < 2:
    print(a*b)


def string_rep(str, v):
    if len(str) < 2:
        return str * v
    else:
        return str[:2] * v


print(string_rep('sony', 4))
print(string_rep('R', 4))

"""
24. Write a Python program to test whether a passed letter is a vowel or not
"""

x = str(input("Enter a string character"))
c = ['a','e','i','o','u']
if x in c:
    print("is vowel", x)
else:
    print("It is not a vowel")
















