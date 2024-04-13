n = int(input("Nhập n: "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
        
if s == n:
    print(f"Là số hoàn hảo (s = {s})")
else:
    print(f"Ko là số hoàn hảo (s = {s})")
