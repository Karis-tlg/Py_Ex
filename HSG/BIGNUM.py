def bignum(n, k):
    a = ""
    for i in n:
        if i.isdigit():
            a += i
    return "".join(sorted(a, reverse = True)[:k])

with open("BIGNUM.INP", "r") as f:
    s = f.readline()
    k = int(f.readline())

with open("BIGNUM.OUT", "w") as f:
    f.write(bignum(s, k))
    
