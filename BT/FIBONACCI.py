def fn(n):
	m = [0, 1]
	a, b = 0, 1
	for i in range(3, n + 1):
		c = a + b
		m.append(c)
		a = b
		b = c
	return m 

def fbn(n):
	return fbn(n - 1) + fbn(n - 2)

n = int(input("Nhập n: "))

for i in range(n):
        print(fbn(i))
