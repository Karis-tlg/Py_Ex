v = "AABAAOID"#8
a, b = 0, ""

for i in range(len(v)):
    for j in range(i , len(v)):
        vr = v[i:j + 1]
        #print(f"v[{i}:{j + 1}] = {v[i:j + 1]}")
        if vr == vr[::-1]:
            print(f"v[{i}:{j + 1}] = {v[i:j + 1]}")
            if len(vr) > a:
                a, b = len(vr), vr
            #a = max(a, len(vr))

if a == 0:
    print("Không có xâu đối xứng nào")
else:
    print(f"Xâu con đx dài nhất là `{b}` có độ dài: {a}")
