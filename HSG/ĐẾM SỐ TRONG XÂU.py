n = input("Nhập xâu n: ")
dem = 0
for i in n:
    #if '0' <= i <= '9':
    #if i.isdigit(): #isalpha()
    if i in "0123456789":
        dem += 1
print(dem)
