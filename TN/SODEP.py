def scp(n):
    return int(n ** 0.5) ** 2 == n

with open("SODEP.INP", "r") as f:
    m, n = map(int, f.readline().split())

    a = []
    for i in range(m, n + 1):
        if scp(i + int(str(i)[::-1])):
            a.append(str(i))

with open("SODEP.OUT", "w") as f:
    if len(a) > 0:
        f.write(" ".join(a))
    else:
        f.write("khong co")
