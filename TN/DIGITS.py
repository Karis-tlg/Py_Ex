def cv(n):
    for i in n:
        if 0 <= int(i) <= 9:
            a[int(i)] += 1

a = [0] * 10    

n = int(input())

for i in range(1, n + 1):
    cv(str(i))

for i in range(10):
    print(i, a[i])
        
