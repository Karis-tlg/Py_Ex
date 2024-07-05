import requests, re

headers = {
    "Accept-Encoding": "identity",
    "Accept-Language": "en",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; BEDROCK-UPDATER)"
}

url = "https://minecraft.net/en-us/download/server/bedrock/"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    content = response.text
    
    download_url = re.search(r'https://minecraft\.azureedge\.net/bin-linux/[^"]*', content)
    
    if download_url:
        print("Download URL:", download_url.group(0))
    else:
        print("No download URL found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


