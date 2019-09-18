"""
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""
print(abs.__doc__)

"""
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

import calendar
m = int(input("Enter a month name: "))
y = int(input("Enter a year number: "))
print(calendar.month(y, m))

"""
13. Write a Python program to print the following "here document".
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
print("""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")
