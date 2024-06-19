def sang(m, n):
    if n < 2:
        n = 2
    a = [True] * (n + 1)
    a[0], a[1] = False, False
    for i in range(m, int(n ** 0.5) + 1):
        if a[i] == True:
            for j in range(i * i, n + 1, i):
                a[j] = False

    b = []
    for i in range(max(2, m), n + 1):
        if a[i]:
            b.append(i)
    return b

m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

print(sang(m, n))


    
