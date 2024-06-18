n = int(input())
a = list(map(float, input().split()))

t = sum(a)/len(a)

for i in sorted(a):
    if i > t:
        print(t, i, a.index(i) + 1)
        break