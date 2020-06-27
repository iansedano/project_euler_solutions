
fibo1 = 1
fibo2 = 2
fibo3 = 3
fiboX = 0
fiboSum = 0

while (fibo2 < 4000000):
    if (fibo2 % 2) == 0:
        fiboSum = fiboSum + fibo2
        fiboX = fibo3 + fibo2
        fibo1 = fibo2
        fibo2 = fibo3
        fibo3 = fiboX
    else:
        fiboX = fibo3 + fibo2
        fibo1 = fibo2
        fibo2 = fibo3
        fibo3 = fiboX

print (fiboSum)


    
    
