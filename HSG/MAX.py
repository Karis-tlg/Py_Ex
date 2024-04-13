def max(x):
    smax = x[0]
    for i in x:
        if i > smax:
            smax = i
    return smax

n = input("Nhập n: ").split()
a = []
for i in n:
    a.append(int(i))
print(max(a))
