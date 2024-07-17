from PIL import Image
import numpy as np
import os

def convert_image(input_path):
    directory = os.path.dirname(input_path)
    filename, extension = os.path.splitext(os.path.basename(input_path))
    
    original_image_path = input_path
    converted_image_path = os.path.join(directory, f"{filename}{extension}")  
    
    image = Image.open(original_image_path).convert("RGBA")
    image_array = np.array(image)

    height, width, channels = image_array.shape
    enlarged_array = np.zeros((height * 2, width * 2, channels), dtype=np.uint8)

    enlarged_array[::2, ::2] = image_array
    enlarged_array[1::2, ::2] = image_array
    enlarged_array[::2, 1::2] = image_array
    enlarged_array[1::2, 1::2] = image_array
    
    enlarged_image = Image.fromarray(enlarged_array, "RGBA")

    enlarged_image.save(converted_image_path)
    
    print(f"Convert done: {converted_image_path}")

input_directory = input("Nhập paht: ")

image_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith('.png')]

for image_file in image_files:
    convert_image(image_file)
