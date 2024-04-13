n = input("Nhập dãy n: ").split()#2 3 4 -> n = ["2", "3", "4"]
a = []
for i in n:
    a.append(int(i))
#a = [2, 3, 4]
dem = 0
for i in a:
    if i % 2 == 0:
        dem = dem + 1
print("Số lượng số chẵn là:",dem)




