n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = []

for i in range(n):
    m.append(a[i])
    m.append(b[i])

for i in set(m):
    print(i, m.count(i))