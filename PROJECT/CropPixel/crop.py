from PIL import Image
import os, shutil

shutil.rmtree('output', True)
os.makedirs('output', exist_ok=True)

def pixelcrop(image):
    bbox = image.getbbox()
    if bbox:
        return image.crop(bbox)
    return image


for filename in os.listdir('input'):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        with Image.open(f"input/{filename}") as img:
            if img.mode == 'RGBA':
                trimmed_image = pixelcrop(img)
                trimmed_image.save(f"output/{filename}")
                print(f"Done: {filename} -> [{trimmed_image.size[0]}, {trimmed_image.size[1]}]")
            else:
                print(f"Skipping: {filename} (No alpha channel)")

print("Processing completed.")
