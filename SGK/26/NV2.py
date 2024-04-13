def prime(n):
    c = 0
    k = 1
    while k < n:
        if n % k == 0:
            c += 1
        k += 1
    if c == 1:
        return True
    else:
        return False

if prime(3) == True:
    print("La so nto")
else:
    print("Khong la so nto")
