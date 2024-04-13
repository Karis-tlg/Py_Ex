n = int(input("n: "))
for i in range(1, n + 1):
    if i**2 == n:
        print(n, "là số chính phương")
        break
else:
    print(n, "không là số chính phương")
