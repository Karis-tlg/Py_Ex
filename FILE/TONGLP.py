with open("TONGLP.INP", "r") as f:
    n = int(f.readline())

with open("TONGLP.OUT", "w") as f:
    t = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if (i ** 3 + j ** 3) == n:
                print(i, j)
                t += 1
