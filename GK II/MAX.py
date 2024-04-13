n = input("Nhập dãy n: ").split()
a = []
for i in n:
    a.append(int(i))
max = a[0]
for i in range(len(a)):
    if a[i] > max and a[i] % 2 == 0:
        max = a[i]
print("Max chẵn là:",max)






