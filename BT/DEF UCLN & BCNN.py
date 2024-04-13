def ucln(m, n):
    while n != 0:
        m, n = n, m % b
    return m

def bcnn(m, n):
    return m * n // ucln(m, n)

a = int(input("a: "))
b = int(input("b: "))

print("Ước chung lớn nhất của hai số là:", ucln(a, b))
print("Bội chung nhỏ nhất của hai số là:", bcnn(a, b))
