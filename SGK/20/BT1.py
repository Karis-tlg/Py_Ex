n = int(input("Nhập n: "))
s = 0
a = 0
for i in range(1, n+1):
    if i % 2 == 0:
        s = s + i
    else:
        a = a + i
print("Tong chan la: ",s)
print("Tong le la: ",a)
