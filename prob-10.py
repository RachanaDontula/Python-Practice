"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
"""
n = int(input("Enter an integer value: "))
i = n + (n*11) + (n*111)
print("The output of n+nn+nnn = ", i)

"""
Python int(x, base=10):
The function returns an integer object constructed from a number or string x, 
or return 0 if no arguments are given. If x is a number, return x.__int__(). 
For floating point numbers, this truncates towards zero.
If x is not a number or if base is given, then x must be a string, bytes, 
or bytearray instance representing an integer literal in radix base
The literal can be preceded by + or - (with no space in between) and surrounded by whitespace
A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35. 
The default base is 10.The allowed values are 0 and 2-36. Base-2, -8, and -16 literals 
can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code.
"""
a = int(input("Enter an integer value: "))
a1 = int("%s" %a)
a2 = int("%s%s" %(a,a))
a3 = int("%s%s%s" %(a,a,a))
b = a1+a2+a3
print(b)

x = str(input("Enter an integer value: "))
x1 = str("%s" %x)
x2 = str(" %s %s" %(x,x))
x3 = str(" %s %s %s" %(x,x,x))
y = x1+x2+x3
print(y)
