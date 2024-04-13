n = 16
for i in range(2, n):
    while n % i == 0:
        print(i, end = " ")
        n = n // i
