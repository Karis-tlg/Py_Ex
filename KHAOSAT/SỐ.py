def uc(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            print(i)
            if n != n // i:
                print(n // i)

def ucln(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

n = 15
uc(n)
