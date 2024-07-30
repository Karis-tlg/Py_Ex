import json

def encode_unicode_except_special(json_obj):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if isinstance(value, str):
                if key not in ['visible', '$menu_name', 'texture']:
                    json_obj[key] = ''.join(['\\u{:04x}'.format(ord(c)) for c in value])
            else:
                encode_unicode_except_special(value)
    elif isinstance(json_obj, list):
        for i, item in enumerate(json_obj):
            if isinstance(item, str):
                json_obj[i] = ''.join(['\\u{:04x}'.format(ord(c)) for c in item])
            else:
                encode_unicode_except_special(item)

def main():
    print("Nhập nội dung JSON (kết thúc nhập bằng dòng trống):")
    input_data = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            input_data.append(line)
        except EOFError:
            break

    json_str = "\n".join(input_data)
    
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Lỗi khi phân tích cú pháp JSON: {e}")
        return

    encode_unicode_except_special(data)

    output_str = json.dumps(data, ensure_ascii=False, indent=2)
    print("\nNội dung đã mã hóa:")
    print(output_str)

if __name__ == "__main__":
    main()
