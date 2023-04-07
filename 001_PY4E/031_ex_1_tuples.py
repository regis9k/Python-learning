# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the 
# addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of 
# (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the 
# person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

name = input("Enter file:")
if len(name) < 1:
    name='mbox_short.txt'
    
handle = open(name)
dic={}
for lines in handle:
    if not lines.startswith('From '):
        continue
    line=lines.rstrip().split()
    mail=line[1]
    dic[mail]=dic.get(mail , 0) + 1
l=[]
for k, v in dic.items():
    l.append((v,k))
l.sort(reverse=True)
person = l[0]
person2=str(person[1])+' '+str(person[0])
print(person2)