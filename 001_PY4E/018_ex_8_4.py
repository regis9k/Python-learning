# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using 
# the split() method. The program should build a list of words. 
# For each word on each line check to see if the word is already 
# in the list and if not append it to the list. When the program 
# completes, sort and print the resulting words in python sort() 
# order as shown in the desired output.

x=open('romeo.txt')
lst=['']
for i in x:
    line=i.split()
    for w in line:
        if w in lst:
            continue
        lst.append(w)
lst=lst[1:]
lst.sort()
print(lst)
