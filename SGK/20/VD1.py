n = int(input("Nhập n: "))
s = 0
for i in range(1, n+1):
    print(f"{i}**3 = {i**3}")
    s += i**3
print(s)

