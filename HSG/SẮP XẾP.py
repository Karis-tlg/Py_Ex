a = [2, 5, 7, 1, 9, 8]
for i in range(1, len(a)):#1 -> 6
    c = a[i]#5
    b = i - 1#0
    while (c < a[b]) and (b >= 0):#5 < 7 and 2 > 0
        a[b +1] = a[b]#1 = 7
        b -= 1#
    a[b + 1] = c
print(a)
