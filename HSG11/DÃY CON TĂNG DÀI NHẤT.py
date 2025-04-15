with open("BAI3.INP", "r") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

    tam = []

    for i in range(len(a) + 1):
        for j in range(i + 1, len(a) + 1):
            if a[i:j] == sorted(a[i:j]) and len(a[i:j]) > len(tam):
                tam = a[i:j]

    print(*tam)
