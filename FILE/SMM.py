def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def ctr(n):
    s = 0
    for i in str(n):
        s += int(i) ** 2
    return snt(s)

with open("SMM.INP", "r") as f:
    n = int(f.readline().strip())

with open("SMM.OUT", "w") as f:
    i = 11
    s = ""
    while n > 0:
        if ctr(i):
            s += f"{i} "
            n -= 1
        i += 1
        
    f.write(s)


