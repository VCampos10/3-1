n1 = int(input('enter your number : '))
n2 = int(input('enter your number : '))
n3 = int(input('enter your number : '))

minval= min(n1, n2, n3)

maxval= max(n1, n2, n3)


if n1 > n2 and n1 > n3:
    n1 = maxval
elif n1 > n2 and n1 < n3:
    median = n1
elif n1 < n2 and n1 < n3:
    n1 = minval
    
print(minval, median, maxval)