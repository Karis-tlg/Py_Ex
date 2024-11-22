import re

def generate_direct_link(share_link):
    return (f"https://drive.google.com/uc?export=view&id={re.search(r'/d/([^/]+)/', share_link).group(1)}" if re.search(r'/d/([^/]+)/', share_link) else None)

direct_link = generate_direct_link(input("Nhập link chia sẻ Google Drive: "))

print(f"Link tải trực tiếp: {direct_link}" if direct_link else "Có cái nịt :))")
