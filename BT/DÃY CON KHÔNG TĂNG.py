def solve(a):
  n = len(a)
  f = [1] * n
  g = [1] * n
  for i in range(1, n):
    f[i] = max(f[j] for j in range(i) if a[j] > a[i]) + 1
    g[i] = max(f[i - 1], g[i - 1]) + 1
  res = max(f[n - 1], g[n - 1])
  i = n - 1
  ans = []
  while i >= 0:
    if f[i - 1] == res:
      i -= 1
    else:
      ans.append(a[i])
      i -= 1
  ans.reverse()
  return ans

n = int(input())
a = list(map(int, input().split()))
res = solve(a)
print(*res)
