import requests as re
import time, os

fp = r"J:\Data\JOBS\đức\PackFiles.zip"
filename = os.path.basename(fp)
file_size = os.path.getsize(fp)

bin_id = "furnace2026"
url = f'https://filebin.net/{bin_id}/{filename}'
headers = {
    "accept": "application/json",
    "Content-Type": "application/octet-stream",
    "cid": "furnace"
}

start_time = time.time()

with open(fp, "rb") as f:
    res = re.post(url, headers=headers, data=f)

end_time = time.time()
upload_time = end_time - start_time

if res.status_code == 201:
    upload_speed = file_size / upload_time / 1024 
    file_url = f"https://filebin.net/{bin_id}/{res.json()['file']['filename']}"
    print(f"OK: {upload_speed:.2f} KB/s\nLink: {file_url}")
else:
    print(f"Error: {res.status_code}, {res.text}")

print(f'Thời gian upload: {upload_time:.2f} giây')
