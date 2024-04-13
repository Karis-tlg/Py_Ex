import requests as re

file = "file.json"
url_up = "https://api.pastes.dev/post"
url_rd = "https://api.pastes.dev"

try:
    with open(file, "r", encoding='utf-8') as f:
        data = f.read()
        
    res = re.post(url_up, headers = {"Content-Type": "text/json"}, data=data)
    
    if res.status_code == 201:
        print(f"URL paste: {url_rd}/{res.json()['key']}")
    else:
        print(f"Đã xảy ra lỗi, mã: {res.status_code}")
        print(f"Thông điệp lỗi: {res.text}")
        
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
