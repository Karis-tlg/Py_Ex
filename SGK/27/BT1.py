def prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
            break
        else:
            return True
        
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
for i in (m, n+1):
    if prime(i):
        print(i, end = " ")
