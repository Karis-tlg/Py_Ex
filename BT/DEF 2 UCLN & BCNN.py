def ub(m, n):
    c = m * n
    while n != 0:
        m, n = n, m % n
    d = c // m
    return m, d

a = int(input("a: "))
b = int(input("b: "))

ucln, bcnn = ub(a, b)

print("Ước chung lớn nhất của hai số là:", ucln)
print("Bội chung nhỏ nhất của hai số là:", bcnn)
