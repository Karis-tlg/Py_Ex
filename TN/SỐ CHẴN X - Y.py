x = int(input())
y = int(input())

a = []

for i in range(x, y + 1):
    if i % 2 == 0 and i % 3 == 0:
        a.append(i)

print(*a)
print(f"Co tat ca: {len(a)} so")
