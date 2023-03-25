# merged two programs from before

###

count = 0
total = 0
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
        smallest = num
    
    # largest
    if num>largest:
        largest=num
    
    # smallest
    if num<smallest:
        smallest=num

        # total
    total=total+num

    # count
    count=count+1

print("Maximum is", largest)
print("Minimum is", smallest)
print("Count is", count)
print("Total is", total)
print("Average is", total/count)