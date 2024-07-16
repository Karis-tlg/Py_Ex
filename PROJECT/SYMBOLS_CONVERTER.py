import yaml

def read_yaml_symbols(file_path):
    # Đọc nội dung của file YAML
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    
    # Trích xuất giá trị của các trường symbol
    symbols = {}
    for key, value in data['font_images'].items():
        symbols[key] = value['symbol']
    
    return symbols

def print_symbols(symbols):
    for key, symbol in symbols.items():
        print(f"{key}: {symbol}")

# Đường dẫn tới file YAML
file_path = input('Nhập path: ')

# Đọc và in ra các symbol
symbols = read_yaml_symbols(file_path)
print_symbols(symbols)
