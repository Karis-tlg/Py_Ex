with open("SOTK.INP", "r") as f:
    n, k = map(int, f.readline().split())
    s = sorted(set(list(map(int, f.readline().split()))), reverse=True)

with open("SOTK.OUT", "w") as f:
    f.write(str(s[k - 1]))


    