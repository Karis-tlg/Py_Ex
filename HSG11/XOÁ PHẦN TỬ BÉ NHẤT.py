with open("bai2.inp","r") as f:
    n = int(f.readline())	
    dayso = list(map(int,f.readline().split()))

vitrinho = dayso.index(min(dayso))
l= max(dayso)
dayso[vitrinho]=l
with open ("bai2.out", "w") as f:
    f.write(str(dayso))