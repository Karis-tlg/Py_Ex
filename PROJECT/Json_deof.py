import re
import glob
import os

def deof(n):
    return re.sub(r".", lambda x: r"\u%04X" % ord(x.group()), n)

ext = ("", ".json")

path = input("Nhập path: ")

for file in glob.glob(f"{path}/**/*.json", recursive=True):
    if file.endswith(ext):
        print(file)
