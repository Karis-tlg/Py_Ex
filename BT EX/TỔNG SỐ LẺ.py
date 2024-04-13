a = input("Nhập vào 1 xâu: ")

s = 0
for i in "13579":
    s += int(a.count(i)) * int(i)

print(f"Tổng số lẻ trong xâu là: {s}")





#print(a.count("1") + a.count("3") * 3 + a.count("5") * 5 + a.count("7") * 7 + a.count("9") * 9)
