v = "AABAAOID"
a = 0

for i in range(len(v)):
    for j in range(i , len(v)):
        vr = v[i:j + 1]
        if vr == vr[::-1]:
            if len(vr) > a:
                a = len(vr)
            #a = max(a, len(vr))

if a == 0:
    print("Không có xâu đối xứng nào")
else:
    print("Xâu con đối xứng dài nhất là:", a)
