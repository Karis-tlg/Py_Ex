from PIL import Image
import numpy as np

def convert_image(input_path, output_path):
    image = Image.open(input_path).convert("RGBA")
    image_array = np.array(image)
    print(image_array)

input_path = r"E:\Tin\Py_Ex\PROJECT\FONT\toxic_fumes.png"
output_path = input_path.split('.')[0] + '32x.' + input_path.split('.')[-1]

convert_image(input_path, output_path)


