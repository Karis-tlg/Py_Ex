def tong(n):
    return sum(int(i) for i in str(n))

def sdb(n):
    t = 0
    for i in range(n[0], n[1] + 1):
        if tong(i) == 5:
            t += 1
    return t

with open("SPRIME.INP", "r") as f:
    n = int(f.readline())
    a = []
    for i in range(n):
        a.append(f.readline().strip())
    
    for i in a:
        tam = list(map(int, i.split()))
        print(sdb(tam))

