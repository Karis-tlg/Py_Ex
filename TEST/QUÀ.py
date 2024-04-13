t = "3 6"
s = "10 12 11 5 7 8"

m, n = map(int, t.split())
b = sorted(list(map(int, s.split())))
print(b)
c = float('inf')
for i in range(n - m + 1):
    print(f"for {i} in range({n - m + 1})")
    a = b[i + m - 1] - b[i]
    print(f"b[{i + m - 1}] - b[{i}] | {b[i + m - 1]} - {b[i]} | {b[i + m - 1] - b[i]}")
    if a < c:
        c = a
        print(c)
    #c = min(c, a)


print(str(c))
