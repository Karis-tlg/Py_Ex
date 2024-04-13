n = input("Nhập n: ").split()
a = []
for i in n:
    a.append(int(i))
dem = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])
        dem += 1
print(dem)
