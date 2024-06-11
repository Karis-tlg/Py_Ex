with open("LUCKY.INP", "r") as f:
    n, k = map(int, f.readline().split())
    a = list(map(int, f.readline().split()))

    t = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] + a[j] == k:
                t += 1

with open("LUCKY.OUT", "w") as f:
    f.write(str(t))
