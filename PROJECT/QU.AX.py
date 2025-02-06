import requests as re
import time

# fp = input('Nhập path: ')
fp = r"J:\Data\JOBS\đức\PackFiles.zip"

url = 'https://qu.ax/upload.php'

start_time = time.time()

with open(fp, 'rb') as f:
    files = {'files[]': f}
    res = re.post(url, files=files, data={'expiry': 1})

end_time = time.time()

if res.status_code == 200:
    print('Upload thành công!')
    # print('Response JSON:', res.json()['files'][0]['url'])
    print('Response JSON:', res.json()['files'])
else:
    print('Upload thất bại:', res.status_code)
    print('Response:', res.text)

print(f'Time: {end_time - start_time:.2f}s')
