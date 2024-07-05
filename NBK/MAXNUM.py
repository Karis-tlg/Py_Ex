def find_largest_6_digit_number(s):
    # Nếu chuỗi đầu vào có độ dài nhỏ hơn 6, trả về -1
    if len(s) < 6:
        return -1
    
    # Sử dụng danh sách để lưu các ký tự của số lớn nhất có thể
    result = []
    
    # Số ký tự cần loại bỏ
    num_to_remove = len(s) - 6
    
    for char in s:
        # Trong khi danh sách kết quả không rỗng, số ký tự cần loại bỏ > 0 và ký tự cuối trong danh sách kết quả < ký tự hiện tại
        while result and num_to_remove > 0 and result[-1] < char:
            result.pop()
            num_to_remove -= 1
        result.append(char)
    
    # Nếu vẫn còn số ký tự cần loại bỏ
    while num_to_remove > 0:
        result.pop()
        num_to_remove -= 1
    
    # Ghép các ký tự lại thành chuỗi số
    return ''.join(result[:6])

def main():
    # Đọc dữ liệu vào từ tệp NUMMAX.INP
    with open('NUMMAX.INP', 'r') as infile:
        s = infile.read().strip()
    
    # Tìm số lớn nhất có độ dài 6 ký tự
    result = find_largest_6_digit_number(s)
    
    # Ghi kết quả vào tệp NUMMAX.OUT
    with open('NUMMAX.OUT', 'w') as outfile:
        outfile.write(result if result != -1 else '-1')

# Chạy hàm chính
if __name__ == "__main__":
    main()
