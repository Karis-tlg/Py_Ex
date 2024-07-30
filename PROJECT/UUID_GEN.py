import random

hex_chars = "0123456789abcdef"
uuid = ""
for i in range(32):
    if i in [8, 12, 16, 20]:
        uuid += "-"
    uuid += random.choice(hex_chars)

print(uuid)
