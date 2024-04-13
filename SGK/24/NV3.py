n = int(input("Nhập số học sinh trong lớp: "))
ten = []
hodem = []
for i in range(n):
    s = input(f"Nhập họ tên hs thứ {i+1}: ")
    sline = s.split()
    ten.append(sline[-1])
    del sline[-1]
    hodem.append(" ".join(sline))
print("Danh sách học sinh: ")
for i in range(n):
    print(f"{hodem[i]} | {ten[i]}")
    
    
