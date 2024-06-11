import requests

link = input('Link: ')
path = input('Path: ').replace("\\", "/")

res = requests.get(link, stream=True)

if res.status_code == 200:
    with open(path, 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:  
                f.write(chunk)
    print("Tải video thành công!")
else:
    print("Tải video thất bại.")
