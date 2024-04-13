with open("SOLE_INP.txt", "r") as f:
    s = sum(1 for i in map(int, f.readline().split()) if i % 2 != 0)
#-x    
'''    n = list(map(int, f.readline().split()))
        
s = 0
    
for i in n:
    if i % 2 != 0:
        s += 1
'''
#-x
with open("SOLE_OUT.txt", "w") as f:
    f.write(str(s))