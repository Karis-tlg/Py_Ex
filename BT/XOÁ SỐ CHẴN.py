s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
'''
a = []

for i in range(len(s)):
    if s[i] % 2 != 0:
        a.append(s[i])
s = a
'''

while i < len(s):
    if s[i] % 2 == 0:
        del s[i]
    else:
        i += 1

print("Danh sách sau khi xoá các phần tử chẵn:", s)
