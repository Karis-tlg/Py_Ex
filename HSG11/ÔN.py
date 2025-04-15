ss = int(input())
n = ss // 86400
h = (ss % 86400) // 3600
p = (ss % 3600) // 60
s = ss % 60

print(f"{n} ngày, {h} giờ, {p} phút, {s} giây")
