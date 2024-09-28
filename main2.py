n1 = int(input('enter your first number : '))
n2 = int(input('enter your second number : '))
n3 = int(input('enter your third number : '))
# input numbers
minval= min(n1, n2, n3)

maxval= max(n1, n2, n3)


if n1 > n2 and n1 > n3:
    n1 = maxval
elif n1 > n2 and n1 < n3:
    median = n1
elif n1 < n2 and n1 < n3:
    n1 = minval
    
print(minval, median, maxval)

#