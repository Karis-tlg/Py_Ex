def sang(m, n):
    if n < 2:
        n = 2
    a = [True] * (n + 1)
    a[0], a[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if a[i] == True:
            for j in range(i * i, n + 1, i):
                a[j] = False

    b = []
    for i in range(max(2, m), n + 1):
        if a[i]:
            b.append(i)
    return b

def tong(n):
    return sum(int(i) for i in str(n))

def sdb(n):
    t = 0
    for i in sang(n[0], n[1]):
        if tong(i) % 5 == 0:
            t += 1
    return t

with open("SPRIME.INP", "r") as f:
    n = int(f.readline().strip())
    c = []
    for i in range(n):
        c.append(list(map(int, f.readline().strip().split())))

with open("SPRIME.OUT", "w") as f:
    for i in c:
        f.write(str(sdb(i)))
