def enc(s):
    a = []
    i = 0
    while i < len(s):
        t = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            t += 1
        a.append(str(t) + s[i])
        i += 1
    return ''.join(a)

n = int(input().strip())
s = input().strip()

for i in range(n):
    s = enc(s)

print(s)
