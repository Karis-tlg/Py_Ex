N = int(input("Nhap N: "))
a = []
for i in range(N):
    a.append(int(input(f"Nhap so {i+1}: ")))
print(a)
i = 0
while i < len(a):
    if a[i] % 3 == 0:
        #print(a[i])
        a.remove(a[i])
        a.insert(i, 0)
        a.insert(i + 1, 0)
        a.insert(i + 2, 0)
        i += 2
        #print(a)
        #print(i)
    print(a[i])
    i += 1
    
#print(a)
