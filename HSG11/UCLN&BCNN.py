import math

a, b = list(map(int, input("Nhập a, b: ").split()))
print(f"BCNN của {a} và {b} là: {math.lcm(a, b)}")
print(f"UCLN của {a} và {b} là: {math.gcd(a, b)}")