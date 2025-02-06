import os
import zipfile
import requests

ngrok_url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip"
ngrok_zip = "ngrok.zip"
ngrok_bin = "ngrok"

print("🔹 Đang tải Ngrok...")
response = requests.get(ngrok_url, stream=True)
with open(ngrok_zip, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        file.write(chunk)

print("🔹 Đang giải nén Ngrok...")
with zipfile.ZipFile(ngrok_zip, "r") as zip_ref:
    zip_ref.extractall(".")

print("🔹 Cấp quyền thực thi...")
os.chmod(ngrok_bin, 0o755)
os.remove(ngrok_zip)

print("✅ Ngrok đã được cài đặt thành công!")
