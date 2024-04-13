with open("CHIA_QUA.INP", "r") as f:
    m = int(f.readline())
    n = list(map(int, f.readline().split()))
    
s = sum(n)

if s % 2 == 0:
    v = "YES"
else:
    v = "NO"

with open("CHIA_QUA.OUT", "w") as f:
    f.write(v)

