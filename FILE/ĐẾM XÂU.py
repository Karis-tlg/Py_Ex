with open("XAU_INP.txt", "r") as f:
    n = list(f.readline())
    
c = sum(1 for i in n if i.isalpha())
s = sum(1 for i in n if i.isdigit())

'''
for i in n:
    if i.isalpha():
        c += 1
    elif i.isdigit():
        s += 1
'''

with open("XAU_OUT.txt", "w") as f:
    f.write(f"{c}\n{s}")
