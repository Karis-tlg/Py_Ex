import os

def rename_files(prefix, folder_path):
    if not os.path.isdir(folder_path):
        print("Đường dẫn thư mục không tồn tại.")
        return

    num = 1  
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            new_name = f"{prefix}{num}.csv"
            old_file = os.path.join(folder_path, file)
            new_file = os.path.join(folder_path, new_name)
            os.rename(old_file, new_file)  
            print(f"Đổi: {file} -> {new_name}")
            num += 1  


prefix = input("Nhập tên: ")
folder_path = input("Path: ")

rename_files(prefix, folder_path)
