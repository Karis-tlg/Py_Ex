n = list(map(int, input().split()))

a = []

for i in n:
    if n.count(i) > 1:
        a.append(i)

#print(*a)
print(*set(a))
