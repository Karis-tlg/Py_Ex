import requests as re
from PIL import Image, ImageDraw, ImageFont, ImageColor

while True:
#    address = input("Nhập ip: ")
    address = "mco.cubecraft.net"
    url = f"https://api.mcsrvstat.us/3/{address}"
    if re.get(url, timeout=300).json()["online"] == True:
        break
    else:
        print("Vui lòng kiểm tra lại ip và port")

status = re.get(url, timeout=300).json()
desc = f"Online: {str(status['online']).capitalize()}"
desc += f"\nIP: {status['ip']}"
if "hostname" in status:
    desc += f"\nHost: {status["hostname"]}"
desc += f"\nPort: {status['port']}"
if "protocol" in status:
    if "name" in status["protocol"]:
        desc += f"\nVersion: {status['protocol']['name']}({status['protocol']['version']})"
    else:
        desc += f"\nVersion: {status['protocol']['version']}"
else:
    desc += f"\nVersion: {status['version']}"
if "software" in status:
    desc += f"\nSoftware: {status['software']}"
    desc += f"\nPlayers: {status['players']['online']}/{status['players']['max']}"
    desc += f"\nMotd:\n" + "\n".join(status["motd"]["clean"]) 

desc += f"\n\n\n\nInfor:\n" + "\n".join(status["info"]["clean"]) 


img = Image.new(mode="RGBA", size=(300, 300), color='ghostwhite')

font = ImageFont.truetype('C:\\Users\\Admin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\MinecraftRegular-Bmg3.otf', 10)

draw = ImageDraw.Draw(img)
draw.text((10, 10), desc, font=font, fill =(50, 168, 82))
img.save("C:\\Users\\Admin\\Desktop\\Tin\\PROJECT\\yes.png")
img.show()



print(desc)
