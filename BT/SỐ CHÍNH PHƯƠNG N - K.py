#import math as m

#n, k = map(int, input().split())

t = "20 1"
n, k = map(int, t.split())
s = 0

for i in range(k, n+1):
#    if m.isqrt(i) ** 2 == i:
    if int(i**0.5) ** 2 == i:
        print(i, end = " ")
        s += 1
        
print(/ns)
