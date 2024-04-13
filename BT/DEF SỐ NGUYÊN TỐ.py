def snt(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("n: "))

if snt(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong la so nguyen to")
