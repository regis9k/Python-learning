#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# chop:
x=['seihjfbi','seofjknioj','awdawda','awd2dawda']
def chop(x):
    del x[0]
    del x[-1]
y=chop(x)
print('chop values:')
print(y)
print(x,'\n')

# middle
z=['seihjfbi','seofjknioj','awdawda','awd2dawda']
def middle(z):
    nz=z[1:-1]
    return(nz)

print('middle values:')
print(middle(z))
print(z,'\n')