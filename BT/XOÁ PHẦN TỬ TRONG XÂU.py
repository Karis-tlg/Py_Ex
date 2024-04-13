n = input("Nhập dãy n: ").split()
k = int(input("Nhập số k: "))
a = []
for i in n:
    a.append(int(i))
if k >= 0 and k < len(a):
    del a[k]
else:
    print("Nhập lại k")
    
