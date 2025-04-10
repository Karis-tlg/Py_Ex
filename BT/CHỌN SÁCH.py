t = "5 3"
s = "4 7 2 9 3"
n, m = map(int, t.split())

b = sorted(list(map(int, s.split()))) 

n = b[m - 1] - b[0]  

print(n)