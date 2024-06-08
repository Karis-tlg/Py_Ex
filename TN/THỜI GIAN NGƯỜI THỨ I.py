N = int(input("Nhap N: "))
m = int(input("Nguoi thu i: "))
a = []
for i in range(N):
    a.append(int(input(f"Nhap T{i+1}: ")))

print(f"Thoi gian nguoi thu {m} phai cho la {sum(a[0:m-1])}")
