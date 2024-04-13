import math
with open("SIEUNT.INP") as a:
    d = a.read()

def fact(val):
    f = []
    for x in range(1, round(math.sqrt(val))):
        if val % x == 0:
            f.append(x)
    return f

def prime(inp):
    if inp < 2 or inp % 2 == 0 or len(fact(inp)) > 1:
        return False
    else:
        return True

def superprime(i):
    if prime(i) and prime(int(str(i)[::-1])):
        return True
    else:
        return False

res = []
for x in d.split("\n"):
    x = list(map(int, x.split()))
    dat = []
    for y in range(x[0], x[1] + 1):
        if superprime(y):
            dat.append(y)
    if dat == []:
        dat.append(-1)
    res.append(" ".join(list(map(str, dat))))


with open("SIEUNT.OUT", "w") as a:
    d = a.write("\n".join(res))