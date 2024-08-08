n = int(input("Nhập n: "))
k = list(map(int, input("Nhập k: ").split()))

t = 0

for i in range(len(k) + 1):
    for j in range(i + 1, len(k) + 1):
        if sum(k[i:j]) == 0:
            print(k[i:j])
            t += 1
print(t)
