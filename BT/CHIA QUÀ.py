m = int(input())
n = list(map(int, input().split()))

s = sum(n)

if s % 2 == 0:
    print("YES")
else:
    print("NO")

