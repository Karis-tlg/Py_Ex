N = int(input("Nhap n: "))
a = []
for i in range(N):
    a.append(int(input(f"Nhap so {i+1}: ")))

print(a)
b = []
for i in a:
    if i % 3 != 0:
        b.append(i)
    
print(b)
        
