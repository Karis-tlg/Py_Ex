import math as m

n = int(input())
a = [int(input()) for i in range(n)]

t = 0
for i in range(1, max(a)):
    if all(m.gcd(i, j) == 1 for j in a):
        t = i

print(t)
    
