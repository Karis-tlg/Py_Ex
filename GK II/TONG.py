n = input("Nhập dãy n: ").split()
tong = 0
a = []
for i in n:
    a.append(int(i))
for i in a:
    if i % 2 == 0:
        tong = tong + i
print("Tổng chẵn là:",tong)






