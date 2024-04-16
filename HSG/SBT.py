def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tong(n):
    t = 0
    for i in str(n):
        t += int(i)
    return t

def tongbp(n):
    s = 0
    for i in str(n):
        s += int(i)**2
    return s
    
def sbt(n, m):
    dem = 0
    for i in range(n, m+1):
        if snt(tong(i)) and snt(tongbp(i)):
            dem += 1
    return str(dem)

with open("SBT.INP", "r") as f:
    l, r = list(map(int, f.read().split()))
    
with open("SBT.OUT", "w") as f:
    f.write(sbt(l, r))
