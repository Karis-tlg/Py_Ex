def tong(n):
    return sum(int(i) for i in n)

with open("EXLIST.INP", "r") as f:
    n = int(f.readline().strip())
    m = list(map(int, f.readline().split()))

    s, t = "", 0
    
    for i in range(len(m)):
        for j in range(i, len(m)):
            a = m[i:j + 1]
            if a[0] == a[-1]:
                if len(a) > len(s) or (len(a) == len(s) and sum(a) > t):
                    s = a
                    t = sum(a)

with open("EXLIST.OUT", "w") as f:
    f.write(f"{len(s)} {t}")



