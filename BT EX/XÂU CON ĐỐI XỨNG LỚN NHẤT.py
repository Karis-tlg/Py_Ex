n = "AABAAOID"#8
a = ""

for i in range(len(n)):
    for j in range(i, len(n)):
        nr = n[i:j+1]
        #print(f"n[{i}:{j + 1}] = {n[i:j + 1]}")
        if nr == nr[::-1]:
            print(f"n[{i}:{j + 1}] = {n[i:j + 1]}")
            if len(nr) > len(a):
                a = nr
            #a = max(a, len(nr))

if a == 0:
    print("Không có xâu đối xứng nào")
else:
    print(f"Xâu con đx dài nhất là `{a}` có độ dài: {len(a)}")
