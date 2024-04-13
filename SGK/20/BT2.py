n = int(input("Nhập n: "))#15
s = 0
a = 1
for i in range(1, n):
    if n % i == 0:
        s = s + i
        a = a * i
print("Tong uoc la: ",s)
print("Tich uoc la: ",a)
