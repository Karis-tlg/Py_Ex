import requests as re

link = input("Nhập link cần rút gọn: ")
shorturl = input("*Để trống nếu không muốn tuỳ chỉnh link rút gọn*\nNhập link tuỳ chỉnh: ")
if shorturl == "":
    url = f"https://is.gd/create.php?format=simple&url={link}"
else:
    url = f"https://is.gd/create.php?format=simple&url={link}&shorturl={shorturl}"

try:
    res = re.get(url)
    if res.status_code == 200:
        print("Link rút gọn: ", res.text)
    else:
        print(f"Yêu cầu không thành công. Mã trạng thái: {res.status_code}")
        print(f"Thông điệp lỗi: {res.text}")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
