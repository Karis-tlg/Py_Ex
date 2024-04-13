s = "aHgf2oci6k70x3zJ86kD8m"
a = "26703868"
b = ""

for i in a: 
    c = int(i) - 1
    if c <= 0:
        b += " "
    else:
        b += s[c]

print(b)
