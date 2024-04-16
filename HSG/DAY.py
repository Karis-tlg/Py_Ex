n = int(input())
j = 0
k = 0

while j < n:
    k += 1
    j += k

t = n - (j - k)
re = 1

for i in range(2, k):
    re = re + i - re % i + i * (i - 1)

re = re + k - re % k + k * (t - 1)

if n == 1:
    print(1)
else:
    print(re)
