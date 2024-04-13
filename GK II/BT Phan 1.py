n = []
for i in range(1, 1001):
    if (i % 3 == 0) and (i % 2 != 0):
        n.append(i)
#print(*n)
for i in n:
    if i % 5 == 0:
        n.remove(i)
print(*n)
