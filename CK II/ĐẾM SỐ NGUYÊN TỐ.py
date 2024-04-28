def snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#kha 10a2 (bài 4)
n = int(input("Nhập n: "))
t = 0
for i in range(1, n + 1):
    if snt(i):
        t = t + 1
print(t)



