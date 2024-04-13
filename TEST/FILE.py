with open("INP.txt", "r") as f:
    a = f.readlines()
    n = int(a[0])
    m = list(map(int, a[1].split()))

s = sum(m)

with open("OUT.txt", "w") as f:
    f.write(str(s))
    
