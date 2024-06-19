def sang(n):
    a = [True] * (n + 1)
    a[0], a[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if a[i] == True:
            for j in range(i * i, n + 1, i):
                a[j] = False
    return a

n = int(input("Nhap n: "))

for i in range(n + 1):
    if sang(n)[i]:
        print(i, end = " ")


    
