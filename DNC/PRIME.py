def snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main(n):
    t = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if snt(i):
                t += 1
    return t

with open("PRIME.INP", "r") as f:
    n = int(f.readline())
    m = list(map(int, f.readline().split()))
    s, a = 0, 0
    for i in m:
        if main(i) > s:
            s = main(i)
            a = i
            
with open("PRIME.OUT", "w") as f:
    f.write(str(a))
    
