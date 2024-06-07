s1 = input('Mời nhập xâu: ')
k = ''
s2 = ''
for x in s1:
    if x!=k:
        #print(x)
        s2 = s2 + x
        print(s2)
        k = x
        #print(k)
print('Xâu kết quả là:',s2)
