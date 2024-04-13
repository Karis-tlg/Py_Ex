s = "AxK2f3M0N345njS12KJ"
n = 0


for i in s:
    if i.isdigit():
        n += int(i)
        
"""    if '0' <= i <= '9':
        n += int(i)
"""

print("Số bí mật là:", n)
