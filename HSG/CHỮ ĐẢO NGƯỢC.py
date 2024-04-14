def dn(n):
    return n[::-1]
def ktr(n):
    if n[::-1] == n:
        return True
    return False

n = input("Nhập xâu n: ").split()

print("Chữ đn là: ",*dn(n))

if ktr(n):
    print(*n,"là chữ đảo ngược")
else:
    print(*n,"ko là chữ đảo ngược")


