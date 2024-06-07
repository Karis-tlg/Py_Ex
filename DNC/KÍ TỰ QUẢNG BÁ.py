def cstr(s):
    i = 0
    n = len(s)
    while i < n:
        if s[i:i+3] == "FDD":
            i += 3
        elif s[i:i+2] == "FD":
            i += 2
        elif s[i] == "F":
            i += 1
        else:
            return False
    return True

n = int(input().strip())
a = []
    
for i in range(n):
    s = input().strip()
    if cstr(s):
        a.append("Yes")
    else:
        a.append("No")
    
for i in a:
        print(i)


