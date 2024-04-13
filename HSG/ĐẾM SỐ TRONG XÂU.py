n = input("Nhập xâu n: ")
dem = 0
for i in n:
    if '0' <= i <= '9':
        dem += 1
print(dem)
