a = int(input("a: "))
b = int(input("b: "))
t = a*b
bcnn = 0

'''
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
    print(b)
'''

while b != 0:
    a, b = b, a % b
   
bcnn = t // a

print("Ước chung lớn nhất của hai số là:", a)
print("Bội chung nhỏ nhất của hai số là:", bcnn)
