n = list(map(int, input().split()))

a = []

for i in n:
    if i not in a:
        a.append(i)

print(*a)
#print(set(a)