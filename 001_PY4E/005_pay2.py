# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
def computepay(h, r):
  hr = h
  hour = float(hr)
  rte = r
  rate = float(rte)
  if (hour > 40.0):
    pay1 = 40.0 * rate
    pay2 = ((hour - 40) * rate * 1.5)
    pay3 = (pay1) + (pay2)
    return pay3
  else:
    pay4 = hour * rate
    return pay4


h = input('Enter hours: ')
try:
  z = float(h)
except:
  print('Error, please enter numeric input')
  quit()

r = input('Enter rate: ')
try:
  z = float(r)
except:
  print('Error, please enter numeric input')
  quit()

print('Pay', computepay(h, r))