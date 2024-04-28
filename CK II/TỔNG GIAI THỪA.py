#'''
def gt(n):
    if n == 0 or n == 1:
        return 1
    return n * gt(n - 1)
#kha 10a2 (bài 1)
n = int(input("Nhập n: "))
t = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        t += gt(i)
print(t)

'''
def gt(n):
    if n == 0 or n == 1:
        return 1
    return n * gt(n - 1)

n = int(input("Nhập n: "))
t = sum(gt(i) for i in range(2, n + 1, 2))
print(t)
'''
