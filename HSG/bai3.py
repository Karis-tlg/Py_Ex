lst = [5, 8, 6, 8, 2, 5, 7, 9, 4]
n = 9
tam = []
ans = []
dem = 0
count = 0

for i in range(n-1):
    if lst[i+1] >= lst[i]:
        tam.append(str(lst[i]))
    elif lst[i+1] <= lst[i]:
        tam.append(str(lst[i]))
        if len(tam) >= count:
            count = len(tam)
            ans = tam
            tam = []
print(' '.join(ans))
        
        
