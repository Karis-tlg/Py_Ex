FI = 'BUS.INP'
FO = 'BUS.OUT'

with open(FI, 'r') as f:
    n, d, t = map(int, f.readline().split())
    a = list(map(int, f.read().split()))


with open(FO, 'w') as f:
    for i in range(n):
        if a[i] <= t:
            f.write('1 ')
        else:
            a[i] -= t
            q = a[i] // d
            w = a[i] % d
            if w == 0:
                f.write(f'{q + 1} ')
            else:
                f.write(f'{q + 2} ')
