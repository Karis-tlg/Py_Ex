tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

def f(a, b):
    while b != 0:
        a, b = b, a % b
    return a

ucln = f(tu, mau)

print(f"{tu}/{mau} = {tu // ucln}/{mau // ucln}")
