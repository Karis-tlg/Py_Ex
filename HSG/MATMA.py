def tong(n):
    t = 0
    for i in n:
        if i.isdigit():
            t += int(i)
    return str(t)

def xau(n):
    a = ""
    for i in n:
        if i.isalpha() or i == " ":
            a += i
    return " ".join(a[::-1].split()[::-1])

with open("MATMA.INP", "r") as f:
    n = f.readline()

with open("MATMA.OUT", "w") as f:
    f.write(tong(n) + " " + xau(n))
    
