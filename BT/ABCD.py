def main(A, B, C, D):
    if B < C:
        return 0
    elif A >= D:
        return (B - A + 1) * (D - C)

    m = max(0, min(B, D) - max(A, C) + 1)
    n = (B - A + 1) * (D - C + 1)

    return n - m

A, B, C, D = map(int, input().split())
s = main(A, B, C, D)
print(s)
