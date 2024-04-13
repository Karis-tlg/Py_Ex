import sys
filename = "GIAIMA"
sys.stdin = open(f"{filename}.INP", "r")
sys.stdout = open(f"{filename}.OUT", "w")

dixt = {97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}
a = input()
sp = []
x = 0
while x != len(a):
    if a[x] == "9":
        sp.append(int(a[x] + a[x + 1]))
        x += 2
    else:
        sp.append(int(a[x] + a[x + 1] + a[x + 2]))
        x += 3

r_sp = []
for x in sp:
    r_sp.append(dixt[x])
print("".join(r_sp))