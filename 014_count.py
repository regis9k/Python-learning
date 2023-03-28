#Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(str,char):
    c = 0
    for i in str:
        if i == char:
            c = c + 1
    return(c)

print(count('banan','a'))