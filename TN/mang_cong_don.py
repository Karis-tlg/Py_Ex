#Sử dụng mảng cộng dồn:

N=1000002
s=[0]*N
n = int(input())
for i in range(1,n+1):
    m=int(input())
    s[i]=s[i-1]+m

m=int(input())
for i in range(1,m+1):
    l=int(input())
    r=int(input())
    print(s[r]-s[l-1])