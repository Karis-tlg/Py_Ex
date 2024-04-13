s = "Tinhoc95Tre68nam2023"
k = 3
a = []
b = []

for i in s:
    if i.isdigit():
        a.append(i)

for i in a:
    while k > 0 and b[-1] < i:
        b.pop()
        k -= 1
    b.append(i)

result_str = ''.join(map(str, b))

print(int(result_str))
    


