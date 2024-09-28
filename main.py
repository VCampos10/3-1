# enter all inputs (3)
number1 = int(input('Enter your number : '))
number2 = int(input('Enter your number : '))
number3 = int(input('Enter your number : '))

minval = min(number1, number2, number3)
maxval = max(number1, number2, number3)


if (number1 != minval and number1 != maxval):
    median = number1
elif (number2 != minval and number2 !=maxval):
    median = number2
elif (number3 != minval and number3 != maxval):
    median = number3
    
print(minval, median, maxval)

#
