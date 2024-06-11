with open("PITAGO.INP", "r") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    t = 0

    b = [i ** 2 for i in a]

    for i in range(len(a)):
        for j in range(i, len(a)):
            if (a[i] ** 2 + a[j] ** 2) in b:
                t += 1

with open("PITAGO.OUT", "w") as f:
    f.write(str(t))
    
