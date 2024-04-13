import requests
from pathlib import Path

string_path = input("Nhập path đến file: ")

res = requests.post(
    url=r'https://file.io',
    files={
        'file': Path(string_path).read_bytes(),
        'id': 'f8e7d567-ad05-4998-ae1c-f0a5c4097495',
        'key': 'PVXUJLD.KGTKTCZ-WZB417X-K7JK4FC-CQ36NX8',
        'maxDownloads': 1
    }
)
print(res.json())
