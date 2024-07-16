import requests as re

fp = input('Nhập path: ')

url = 'https://qu.ax/upload.php'

with open(fp, 'rb') as f:
    files = {'files[]': f}
    res = re.post(url, files=files)

if res.status_code == 200:
    print('Upload thành công!')
    print('Response JSON:', res.json()['files'][0]['url'])
else:
    print('Upload thất bại:', res.status_code)
    print('Response:', res.text)
