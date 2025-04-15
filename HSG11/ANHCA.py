with open("ANHCA.INP", "r") as f:
    s = f.readline()
with open("ANHCA.OUT", "w") as f:
    print("".join(sorted(s, reverse=True)))
