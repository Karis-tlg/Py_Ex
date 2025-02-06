import requests
import time
import os
import hashlib

fp = r"J:\Data\JOBS\đức\PackFiles.zip"
filename = os.path.basename(fp)
file_size = os.path.getsize(fp)

api_key = "z4ykmkgYnbX4V6rx"
url = "https://lobfile.com/api/v3/upload.php"
headers = {
    "X-API-Key": api_key
}

start_time = time.time()

with open(fp, "rb") as f:
    files = {"file": (filename, f)}
    res = requests.post(url, headers=headers, files=files)

end_time = time.time()

upload_time = end_time - start_time

if res.status_code == 200:
    if res.json().get("success"):
        upload_speed = file_size / upload_time / 1024  
        print(f"OK: {upload_speed:.2f} KB/s\nLink: {res.json().get('url')}")
    else:
        print(f"Error: {res.json().get('error')}")
else:
    print(f"Error: {res.status_code}, {res.text}")

print(f'Thời gian upload: {upload_time:.2f} giây')
