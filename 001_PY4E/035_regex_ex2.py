# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. 
# Compute the average of the numbers and print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756

import re
inp=input('Enter file:')
if len(inp) < 1:
    inp = 'mbox_short.txt'
fhandle = open(inp)
numbers=[]
for line in fhandle:
    number = re.findall('New Revision: ([0-9]+)', line)
    if len(number) > 0:
        numbers=numbers + number
numbers = [int(number) for number in numbers]
print(int(sum(numbers) / len(numbers)))