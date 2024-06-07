def enc(s):
    a = []
    t = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            t += 1
        else:
            a.append(str(t) + s[i - 1])
            t = 1
    a.append(str(t) + s[-1])  
    return ''.join(a)

n = int(input().strip())
s = input().strip()

for i in range(n):
    s = enc(s)

print(s)
