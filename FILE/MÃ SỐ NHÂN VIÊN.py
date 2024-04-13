with open('CODE.INP', 'r') as f:
    n = int(f.readline())
    m = sorted([int(f.readline()) for i in range(n)])

a = 1
for i in m:
    if i == a:
        a += 1
    else:
        with open('CODE.OUT', 'w') as f:
            f.write(str(a))
        break
    


