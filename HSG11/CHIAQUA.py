with open("CHIAQUA.INP", "r") as f:
    n = int(f.readline())
    t = sum(int(i) for i in f.readline().split())

    '''t = 0
    a = f.readline().split()
    for i in range(n):
        t += int(a[i])'''
    

with open("CHIAQUA.OUT", "w") as f:
    '''f.write(str(int(t/2))) 
    f.write(" ")
    f.write(str(t - int(t/2)))'''

    f.write(f"{str(int(t/2))} {str(t - int(t/2))}")