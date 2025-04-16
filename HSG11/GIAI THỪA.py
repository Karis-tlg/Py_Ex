with open("GTHUA.INP", "r") as f: 
    n = int(f.readline())  

t = 0
gt = 1 
for i in range(1, n + 1):
    gt *= i
    if i % 2 == 0:
        t += gt

with open("GTHUA.OUT", "w") as f: 
    f.write(str(t))