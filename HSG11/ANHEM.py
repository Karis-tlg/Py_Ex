def sang(n):
    snt = [True] * (n + 1)
    snt[0] = snt[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if snt[i]:
            for j in range(i * i, n + 1, i):
                snt[j] = False
    return snt

with open("ANHEM.INP", "r") as f:
    n, k = map(int, f.readline().split())

snt = sang(n)

t = 0
for i in range(2, n - k + 1):
    if snt[i] and snt[i + k]:
        t += 1

with open("ANHEM.OUT", "w") as f:
    f.write(str(t))
