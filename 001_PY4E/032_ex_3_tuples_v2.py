# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. Your program 
# should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples 
# from several different languages and see how letter frequency varies between languages. Compare your 
# results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
x='mbox_short.txt'
fhandle=open(x)
dir={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
for line in fhandle:
    for letter in line:
        letter=letter.lower()
        if letter in dir:
            dir[letter]=dir[letter] + 1
        else:
            continue
letters=[]
for k, v in dir.items():
    letters.append((v, k))
letters.sort(reverse=True)
for i in letters[:5]:
    print (i)