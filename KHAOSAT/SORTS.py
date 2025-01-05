def bubbleSort(n):
    for i in range(len(n) - 1):
        for j in range(len(n) - i - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
                print(n)

n = [5, 8, 6, 3, 7]
bubbleSort(n)
