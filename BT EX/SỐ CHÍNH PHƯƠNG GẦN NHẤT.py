v = int(input("Nhập vào 1 số: "))
a = int(v**0.5)**2
b = int(v**0.5 + 1)**2 

print(a, b)
if v - a < b - v:
    print(f"Số chính phương gần nhất với {v} là {a}")
else:
    print(f"Số chính phương gần nhất với {v} là {b}")

#print(a if v - a < b - v else b)
