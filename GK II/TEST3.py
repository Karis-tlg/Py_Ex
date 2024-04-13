n = input("Nhập dãy n: ").split()
a = []
for i in n:
    a.append(int(i))
k = int(input("Nhập số k: "))
if k < len(a):
    del a[k]
    print(a)
else:
    print("Vui lòng nhập lại số k")
