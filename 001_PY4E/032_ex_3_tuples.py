# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. Your program 
# should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples 
# from several different languages and see how letter frequency varies between languages. Compare your 
# results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
x='mbox_short.txt'
fhandle=open(x)
dir={}
for line in fhandle:
    for letter in line:
        if letter in string.punctuation or letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '\t', '\n']:
            continue
        elif letter == ' ':
            continue
        else:
            letter=letter.lower()
            dir[letter]=dir.get(letter, 0) + 1
letters=[]
for k, v in dir.items():
    letters.append((v, k))
letters.sort(reverse=True)
for i in letters[:5]:
    print (i)