n = " ".join(input("Nhập vào 1 xâu: ").split())
s = ""
for i in n:
    if i.isalnum() or i in [" ", ".", ","]:
        s += str(i)
print(s)
