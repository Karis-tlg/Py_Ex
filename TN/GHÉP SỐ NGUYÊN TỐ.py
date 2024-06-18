def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

a = []

for i in range(1, n + 1):
    if snt(i):
        a.append(i)
        
t = int(f"{a[i - 1]}{a[i]}")

for i in range(1, len(a)):
    t = int(f"{a[i - 1]}{a[i]}")
    if not snt(t):
        print(t)
    
