import glob
import json
import shutil
import os

item_type = ["leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots"]

path = r"E:\JOBS\saly\smp1.zip_Decompiler.com"
pe = r"E:\Tin\Py_Ex\PROJECT\ITEM2D\convert\textures"

a = []

for item in item_type:
    try:
        with open(f"{path}/assets/minecraft/models/item/{item}.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File {item}.json not found.")
        continue

    for override in data.get("overrides", []):
        text = override["model"].replace(":", "/")
        if "ia_auto_gen" in text:
            #a.append(text.split("/")[-1])
            a.append(text)

for i in set(a):
    if "amber" in i:
        print(i)
