def prime(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

for j in range(m, n+1):
    if prime(j):
        print(j, end=" ")
