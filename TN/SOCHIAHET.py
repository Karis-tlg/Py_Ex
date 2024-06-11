def ktr(n):
    t = 0
    for i in str(n):
        if int(i) > 0 and n % int(i) == 0:
            t += 1
    if t == len(str(n)):
        return True
    return False

with open("SOCHIAHET.INP", "r") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    b = []
    
    for i in a:
        if ktr(i):
            b.append(str(i))

with open("SOCHIAHET.OUT", "w") as f:
    f.write(str(len(b)) + "\n")
    f.write(" ".join(b))
