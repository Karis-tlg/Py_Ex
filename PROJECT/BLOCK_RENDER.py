import os
import shutil
from PIL import Image, ImageEnhance

# Định nghĩa các hậu tố của file ảnh png bạn đang sử dụng cho texture mặt khối
up_suffix = "_top"
north_suffix = "_north"
west_suffix = "_west"

# Hàm xử lý hình ảnh
def process_images(input_dir, output_dir):
    # Tạo thư mục output nếu nó không tồn tại
    os.makedirs(output_dir, exist_ok=True)
    
    # Tạo thư mục tạm nếu nó không tồn tại
    tmp_dir = "tmp"
    os.makedirs(tmp_dir, exist_ok=True)

    # Duyệt qua từng file PNG trong thư mục
    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            filepath = os.path.join(input_dir, filename)
            filename_noext = os.path.splitext(filename)[0]

            # Bỏ qua nếu filename chứa các hậu tố
            if any(suffix in filename for suffix in [up_suffix, north_suffix, west_suffix]):
                continue

            print(f"Đang xử lý: {filepath}")

            # Kiểm tra hình ảnh thay thế
            alternative_up = os.path.join(input_dir, filename_noext + up_suffix + ".png")
            alternative_north = os.path.join(input_dir, filename_noext + north_suffix + ".png")
            alternative_west = os.path.join(input_dir, filename_noext + west_suffix + ".png")
            
            # Thiết lập các biến texture dựa trên hình ảnh thay thế hoặc hình ảnh gốc
            top_texture = alternative_up if os.path.exists(alternative_up) else filepath
            north_texture = alternative_north if os.path.exists(alternative_north) else filepath
            west_texture = alternative_west if os.path.exists(alternative_west) else filepath

            # Lật ngang texture mặt trên của khối
            top_img = Image.open(top_texture).transpose(Image.FLIP_LEFT_RIGHT)
            if top_img.mode != 'RGBA':
                top_img = top_img.convert('RGBA')
            top_img.save(os.path.join(tmp_dir, "tmp_top.png"))

            # Làm mặt phía bắc tối hơn một chút
            north_img = Image.open(north_texture)
            if north_img.mode != 'RGBA':
                north_img = north_img.convert('RGBA')
            enhancer = ImageEnhance.Brightness(north_img)
            north_img = enhancer.enhance(0.9)
            north_img.save(os.path.join(tmp_dir, "tmp_north.png"))

            # Làm mặt phía tây tối hơn hai lần
            west_img = Image.open(west_texture)
            if west_img.mode != 'RGBA':
                west_img = west_img.convert('RGBA')
            enhancer = ImageEnhance.Brightness(west_img)
            west_img = enhancer.enhance(0.8)
            west_img.save(os.path.join(tmp_dir, "tmp_west.png"))

            # Tạo khối isometric dưới dạng sprite 2D với viền trong suốt tăng lên
            top_img = Image.open(os.path.join(tmp_dir, "tmp_top.png")).resize((96, 96))
            north_img = Image.open(os.path.join(tmp_dir, "tmp_north.png")).resize((96, 96))
            west_img = Image.open(os.path.join(tmp_dir, "tmp_west.png")).resize((96, 96))

            # Dùng Pillow để tạo hình ảnh isometric
            result = Image.new("RGBA", (128, 128), (0, 0, 0, 0))

            result.paste(top_img, (0, 0), top_img)
            result.paste(north_img, (0, 64), north_img)
            result.paste(west_img, (32, 32), west_img)

            # Lưu kết quả
            result = result.crop((32, 0, 96, 64)).resize((64, 64))
            result.save(os.path.join(output_dir, filename), "PNG")

    # Xóa các file tạm
    shutil.rmtree(tmp_dir)

# Đặt các tham số đầu vào trực tiếp ở đây
input_dir = r"E:\Tin\Py_Ex\PROJECT\input"  # Thay thế <input_directory> bằng thư mục đầu vào của bạn
output_dir = r"E:\Tin\Py_Ex\PROJECT\output"  # Thay thế <output_directory> bằng thư mục đầu ra của bạn

process_images(input_dir, output_dir)
