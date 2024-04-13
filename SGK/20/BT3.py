n = int(input("Nhập n: "))
s = 0
for i in range(1, n+1):
    if i % 2 != 0:
        print(i)
        s += i**2
print(s)
