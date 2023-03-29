# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” 
# is entered, print out the total, count, and average of the numbers. If the user enters anything other 
# than a number, detect their mistake using try and except and print an error message and skip to the next number.

###

count = 0
total = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue
    
    # total
    total=total+num

    # count
    count=count+1

print("Count is", count)
print("Total is", total)
print("Average is", total/count)