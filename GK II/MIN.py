n = input("Nhập dãy n: ").split()
a = []
for i in n:
    a.append(int(i))
min = a[0]
for i in range(len(a)):
    if a[i] < min and a[i] % 2 == 0:
        min = a[i]
print("Min chẵn là:",min)






