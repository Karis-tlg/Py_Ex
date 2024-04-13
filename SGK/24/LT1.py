n = input("Nhập các số cách nhau bởi dấu cách: ")
a = n.split()
s = 0
for i in a:
    i = float(i)
    s += i
print(s)
