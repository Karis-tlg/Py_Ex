def change(ho_ten, c):
    if c == 0:
        return ho_ten.upper()
    else:
        return ho_ten.lower()

ht = input("Nhập họ tên: ")
ct = int(input("Nhập 0 hoặc ...: "))

print(change(ht, ct))
