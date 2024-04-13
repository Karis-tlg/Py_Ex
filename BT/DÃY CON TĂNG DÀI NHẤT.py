n = [5, 8, 6, 8, 2, 5, 7, 9, 4]

if not n:
    print("Dãy con tăng dài nhất: ")
else:
    a = [1] * len(n)
    b = [-1] * len(n)

    for i in range(len(n)):
        for j in range(i):
            if n[j] <= n[i] and a[j] + 1 > a[i]:
                a[i] = a[j] + 1
                b[i] = j

    max_length = max(a)
    max_index = a.index(max_length)

    longest = []
    while max_index != -1:
        longest.insert(0, n[max_index])
        max_index = b[max_index]

    print("Dãy con tăng dài nhất:", ' '.join(map(str, longest)))
