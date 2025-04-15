'''with open("TOUR.INP", "r") as f:
    a = list(map(int, f.readline().split()))
    tmax = tin = a[0]
    b = c = [a[0]]

    for i in range(1, len(a)):
        if tin < 0:
            tin = a[i]
            b = [a[i]]
        else:
            tin += a[i]
            b.append(a[i])

        if tin > tmax:
            tmax = tin
            c = b[:]
    print(c, tmax)'''


with open("TOUR.INP", "r") as f:
    a = list(map(int, f.readline().split()))
    tam = []

    for i in range(len(a) + 1):
        for j in range(i + 1, len(a) + 1):
            if sum(a[i:j]) > sum(tam):
                tam = a[i:j]
    print(*tam)
