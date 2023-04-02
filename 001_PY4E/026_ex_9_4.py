# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's 
#     mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

dic={}
name = input("Enter file:")
if len(name) < 1:
    name = "mbox_short.txt"
handle = open(name)
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    word=words[1]
    dic[word]=dic.get(word,0)+1

count=None
person=None
for ppp,ccc in dic.items():
    if count is None:
        person=ppp
        count=ccc
        continue
    elif ccc > count:
        person=ppp
        count=ccc
print(person, count)