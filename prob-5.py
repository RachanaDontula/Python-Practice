"""
Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them.
"""
first_name = input("Enter your first name: ")
last_name = input("Enter you last name: ")
first_name1 = first_name [::-1]
last_name1 = last_name [::-1]
print("after reversing: ", first_name1, last_name1)
print("After revesing the positions of names: ", last_name + " " + first_name)