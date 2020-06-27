# Find the sum of all the multiples of 3 or 5 below 1000

n = 999
Sum = 0


while (n > 0):
    if ((n%3) == 0) or ((n%5) == 0):
        Sum = Sum + n
        n = n-1
    else:
        n = n-1
        
print(Sum)


