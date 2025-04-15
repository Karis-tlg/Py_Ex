def sch(n):
    for i in str(n):
        if int(i) == 0 or n % int(i) != 0:
            return False
    return True

with open("BAI13.INP", "r") as f:
    n = int(f.readline())
    a = list(map(int , f.readline().split()))

    b = [i for i in a if sch(i)]
    print(*b)