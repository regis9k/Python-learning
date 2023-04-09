import re
numbersstr=list()
handle=open('regex_sum_1777017.txt')
for line in handle:
    line.rstrip()
    numbersstr = numbersstr + (re.findall('[0-9]+',line))
numbers=[]
for number in numbersstr:
    numbers.append(int(number))
print (sum(numbers))


# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )


import re
print(sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_1777017.txt').read())]))