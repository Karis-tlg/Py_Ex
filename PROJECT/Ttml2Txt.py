import xml.etree.ElementTree as ET

def ttml2txt(ttml_file, txt_file):
    tree = ET.parse(ttml_file)
    root = tree.getroot()
    namespaces = {'ttml': 'http://www.w3.org/ns/ttml'}
    
    with open(txt_file, 'w', encoding='utf-8') as txt:
        for i in root.findall('.//ttml:p', namespaces):
            text = ''.join(i.itertext()).strip()
            if text:
                txt.write(text + '\n')


ttml = 'pcmt.ttml'
txt = 'pcmt.txt'
    
ttml2txt(ttml, txt)
print(f"Done")
