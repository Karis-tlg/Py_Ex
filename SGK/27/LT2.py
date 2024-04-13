def tong(a):
    t=0
    for i in range(len(s)):
         t=t+int(a[i])
    return t
def tich(a):
    b = 1
    for i in range(len(a)):
        b = b * int(a[i])
    return b

s = input("Nhập dãy các số: ").split()

print("Tổng a là: ",tong(s))
print("Tích a là: ",tich(s))

