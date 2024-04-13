def dn(n):
    return n[::-1]
def ktr(n):
    if n[::-1] == n:
        return True
    return False

n = input("Nhập xâu n: ")
print(f"Xâu đn là: {dn(n)}")
if ktr(n):
    print(f"{n} là xâu đảo ngược")
else:
    print(f"{n} ko là xâu đảo ngược")
