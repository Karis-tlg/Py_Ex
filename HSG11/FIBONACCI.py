def fib(n):
    if n == 0 or n == 1: return [1]
    
    f = [0] * (n + 1)
    f[0], f[1] = 0, 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f

n = int(input("Nhập n: "))
print(fib(n))

