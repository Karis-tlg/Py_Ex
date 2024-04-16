def pt(n):
    a = ""
    for i in range(2, n):
        while n % i == 0:
            a += str(i) + "*"
            n //= i
    return a.rstrip("*")

with open("FACTOR.INP", "r") as f:
    n = int(f.readline())

with open("FACTOR.OUT", "w") as f:
    f.write(pt(n))
