s = "A79C3e8"
k = 2
a = ""

s = ''.join(sorted(s, reverse = True))

for i in s:
    if "0" <= i <= "9":
        a += i
        
print(a[:k])


