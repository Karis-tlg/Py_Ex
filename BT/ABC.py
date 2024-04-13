N = int(input("Nhập N: "))
print()
S = 0
for A in range(1, N + 1):
    for B in range(1, N + 1):
        C = N - A * B
        if C > 0:
            S += 1
            print(f"{S}. {A} x {B} + {C}")
print(f"\nCác bộ thoả mãn là: {S}")

