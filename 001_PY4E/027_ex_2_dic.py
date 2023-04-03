# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

# Write a program that reads the words in words.txt and stores them as 
# keys in a dictionary. It doesn’t matter what the values are. Then you 
# can use the in operator as a fast way to check whether a string is in the dictionary.

dic={}
count=0
handle=open('romeo.txt')
for lines in handle:
    words=lines.rstrip().split()
    for word in words:
        count=count+1
        dic[word]=count
inp=input('write word to check: ')
if inp in dic:
    print ('word',inp,'is in the file')
else:
    print ('word',inp,'is not in the file')