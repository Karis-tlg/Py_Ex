with open('XINCHAO.INP', 'r') as f:
    n = int(f.readline().strip())
    key = f.readline().strip()
    m = [f.readline().strip() for i in range(n)]

a = []
for x in m:
    i, j = 0, 0
    while i < len(key) and j < len(x):
        if key[i] == x[j]:
            i += 1
        j += 1
    if i == len(key):
        a.append("YES")
    else:
        a.append("NO")

        
print(*a, end = "\n")
'''
with open('XINCHAO.OUT', 'w') as f:
    for result in a:
        f.write(result + "\n")
'''
