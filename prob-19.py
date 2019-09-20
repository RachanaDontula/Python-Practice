"""41. Write a Python program to check whether a file exists."""

import os.path
open('Birthday_reminder.txt', 'w')
print(os.path.isfile('Birthday_reminder.txt'))

"""42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. """


import struct
print(struct.calcsize('P')*8)

"""43. Write a Python program to get OS name, platform and release information"""

import os
import platform
print("OS name: ", os.name)
print("Platform: ", platform.system())
print("Release notes: ", platform.release())

'''44. Write a Python program to locate Python site-packages.'''

import site
print(site.getsitepackages())

"""45. Write a python program to call an external command in Python."""

from subprocess import call
print(call(["ls", "-l"]))

"""46. Write a python program to get the path and name of the file that is currently executing. """

import os
print(os.path.realpath(__file__))

"""47. Write a Python program to find out the number of CPUs using"""

import multiprocessing
print(multiprocessing.cpu_count())

"""48. Write a Python program to parse a string to Float or Integer."""

a = "244.6789"
print(float(a))
print(int(float(a)))

"""49. Write a Python program to list all files in a directory in Python."""


path = 'C:\\Users\\Rachana\\PycharmProjects\\PracticeProblems\\Python-Practice'
files = []
# r = root, d = directory, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.py' in file:
            files.append(os.path.join(r, file))
for f in files:
    print(f)


"""50. Write a Python program to print without newline or space."""
print("***********************")
# or

for i in range(0, 10):
    print("*", end='')


