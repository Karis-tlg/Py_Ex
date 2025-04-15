def snt(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

with open("BAI10.INP", "r") as f:
    n = int(f.readline())
    t = 0 
    i = 1
    while t < n:
        if snt(sum(int(i) ** 2 for i in str(i))):
            #print(sum(int(i) ** 2 for i in str(i)), end = " ")
            t += 1
            print(i, end = " ")
        i += 1