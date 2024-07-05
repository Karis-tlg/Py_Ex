import requests as re

url = "https://api.licensegate.io/license/a1d0b/a78f62e4-c1ad-4dce-8655-9bddd609f1ca/verify"
res = re.get(url)
data = res.json()
    
print(data)

if data['valid']:
  print("ok")
else:
  print("ko")
