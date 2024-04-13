import requests as re

file = "file.json"
url = "https://api.mclo.gs/1/log"
headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json"
}

try:
    with open(file, "r", encoding='utf-8') as f:
        data = f.read()

    res = re.post(url, headers=headers, data=data)

    if res.status_code == 201:
        print(f"URL paste: {res.json()['raw']}")
    else:
        print(f"Failed, status code: {res.status_code}")
        print(f"Error message: {res.text}")

except Exception as e:
    print(f"Error: {e}")
