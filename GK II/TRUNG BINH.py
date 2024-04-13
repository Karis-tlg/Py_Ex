n = input("Nhập dãy n: ").split()
a = []
tong = 0
dem = 0
for i in n:
    a.append(int(i))
for i in a:
    if i % 2 == 0:
        tong = tong + i
        dem = dem + 1
print("Trung bình của số chẵn là:",tong/dem)







