with open("BAI4.INP", "r") as f: 
    s = f.readline()
with open("BAI4.OUT", "w") as f: 
    f.write(str(sum(int(i) for i in s)))

