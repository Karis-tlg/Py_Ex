def sht(n):
    t = 1  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            t += i
            if i != n // i:
                t += n // i
    return t == n and n != 1

for i in range(1, 1000):
    if sht(i): 
        print(i)

'''for i in range(1, 1000):
    t = 0
    for j in range(1, i):
        if i % j == 0:
            t += j
    if t == i:
        print(i)'''