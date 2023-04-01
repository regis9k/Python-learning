# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum 
# and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers 
# the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers 
# after the loop completes.

###

numbers=[]
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue

    numbers.append(num)

print(numbers)
count=len(numbers)
total=sum(numbers)

print("Count is", count)
print("Total is", total)
print("Average is", total/count)