from PIL import Image, ImageColor, ImageFont, ImageDraw

def hex_to_rgb(hex_code):
  """Chuyển đổi mã hex sang giá trị RGB."""
  return tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5))

def draw_text(text, colors, font_path, font_size, image_size):
  """Vẽ văn bản với màu sắc gradient."""
  image = Image.new("RGB", image_size, (255, 255, 255))
  font = ImageFont.truetype(font_path, font_size)
  draw = ImageDraw.Draw(image)  # Thêm dòng này để tạo đối tượng vẽ
  x, y = 0, 0
  for char, color in zip(text, colors):
    char_width, char_height = font.getsize(char)
    draw.text((x, y), char, color, font=font)  # Sử dụng draw.text để vẽ chữ
    x += char_width
  return image

def main():
  # Văn bản hex (đã loại bỏ &)
  text = "084CFBb2064FBi377CFCr4F94FCd66ABFCf7EC3FCl95DBFDoADF3FDp"
  # Chuyển đổi văn bản hex sang chuỗi ký tự
  text = "".join(chr(int(code, 16)) for code in text.split()))
  # Màu sắc
  colors = [hex_to_rgb(code) for code in text[::2]]  # Cắt mỗi ký tự thứ 2

  # Cài đặt font chữ và kích thước
  font_path = "C:\\Users\\Admin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\MinecraftRegular-Bmg3.otf"
  font_size = 32
  # Kích thước ảnh
  image_size = (len(text) * font_size, font_size)

  # Vẽ và hiển thị ảnh
  image = draw_text(text, colors, font_path, font_size, image_size)
  image.show()

if __name__ == "__main__":
  main()
