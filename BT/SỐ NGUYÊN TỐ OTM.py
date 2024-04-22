def snt(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


n = list(map(int, input("Nhap n: ").split()))
a = []

for i in range(n[0], n[1] + 1):
    if snt(i):
        a.append(i)
print(*a)
