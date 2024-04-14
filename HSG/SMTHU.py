def tong(n):
    t = 0
    for i in range(1, n+1):
        if n % i == 0:
            t += i
    return t

with open("SMTHU.INP", "r") as f:
    q = int(f.readline())
    a = list(map(int, f.readline().split()))

with open("SMTHU.OUT", "w") as f:
    for i in range(q):
        f.write(str(tong(a[i])) + " ")
    
