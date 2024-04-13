def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def ktr(n, q):
    digits = [int(d) for d in str(n)]
    a = sorted(digits)
    if q <= len(a):
        return a[q - 1]
    return -1

with open("SO-I.INP", "r") as f:
    N = int(f.readline().strip())
    Q = int(f.readline())

a = ktr(N, Q)
if a == -1:
    print("-1")
elif snt(a):
    print(a, "Yes")
else:
    print(a, "No")
