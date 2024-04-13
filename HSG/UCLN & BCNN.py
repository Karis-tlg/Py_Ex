def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return (a*b) // ucln(a, b)

m = int(input("Nhập a: "))
n = int(input("Nhập b: "))

print(f"UCLN là: {ucln(m, n)}")
print(f"BCNN là: {bcnn(m, n)}")
