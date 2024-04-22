import requests
import os

def download_pack(server_ip, pack_url, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    response = requests.get(pack_url)
    if response.status_code == 200:
        file_name = os.path.basename(pack_url)
        save_path = os.path.join(save_dir, file_name)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Pack đã được tải và lưu vào {save_path}")
    else:
        print("Không thể tải pack từ server Minecraft")

# Địa chỉ IP của server Minecraft
server_ip = "Địa chỉ IP của server Minecraft của bạn"
# URL của pack trên server Minecraft
pack_url = "URL của pack trên server Minecraft"
# Thư mục để lưu pack đã tải về
save_dir = "Thư mục lưu trữ pack"

download_pack(server_ip, pack_url, save_dir)
