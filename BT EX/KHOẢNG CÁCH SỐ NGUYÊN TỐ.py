def pr(v):
    if v < 2:
        return False
    for x in range(2, int(v**0.5) + 1):
        if v % x == 0:
            return False
    return True

v = int(input("Nhập vào 1 số: "))
a = v + 1

while not pr(a):
    a += 1
print(f"Khoảng cách từ {v} đến số nguyên tố tiếp theo ({a}) là: {a - v}")
