"""
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java

Python str.rsplit(sep=None, maxsplit=-1) function:
repr() is  a function to add or represent.

The function returns a list of the words of a given string using a separator as the delimiter string.

If maxsplit is given, the list will have at most maxsplit+1 elements.
If maxsplit is not specified or -1, then there is no limit on the number of splits.
If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
The sep argument may consist of multiple characters.
Splitting an empty string with a specified separator returns [''].
Pictorial Presentation:
"""
file_name = input("Enter a file name: ")
file_extsn = file_name.split(".")
print("The extension of the file given is: ", repr(file_extsn[-1]))
