s = "ABFGHIKLMLKIHGH"
max_length = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i:j+1] == s[i:j+1][::-1]:
            max_length = max(max_length, j - i + 1)

if max_length == 0:
    print("Không có xâu đối xứng nào")
else:
    print("Độ dài của xâu con đối xứng dài nhất là:", max_length)
