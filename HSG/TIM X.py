n = int(input("Nhập n: "))
x = n - 1
while x % 3 != 0:
    x = x - 1
    if x <= 0:
        print("Không có số x")
        break
if x % 3 == 0:
    print(x)
