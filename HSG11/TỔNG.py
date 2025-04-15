with open("TONG.INP", "r") as f:
    t = sum(int(i) for i in f.readline() if i.isdigit())
    
with open("TONG.OUT", "w") as f:
    f.write(str(t))