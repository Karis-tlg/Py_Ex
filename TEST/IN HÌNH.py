p = 5
for i in range(5):
    if p == 1:
        print(" " * i + "#")
    else:
        print(" " * i, end="")
        for j in range(p):
            print("*", end="")
        print()
    if i < 2:
        p -= 2
    else:
        p += -2
