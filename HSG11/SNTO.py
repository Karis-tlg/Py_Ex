def snt(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

with open("BAI6.INP", "r") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    b = [i for i in a if snt(i)]
    print(len(b))
    print(max(b))
    