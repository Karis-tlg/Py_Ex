def maximize_profit(s, k):
    # Tạo danh sách chứa các cặp (giá trị số, vị trí) của các ký tự số
    digits_indices = [(int(s[i]), i) for i in range(len(s)) if s[i].isdigit()]

    # Sắp xếp các cặp này theo giá trị số từ lớn đến bé và vị trí từ bé đến lớn
    digits_indices.sort(reverse=True)

    # Chọn K cặp đầu tiên
    selected_indices = digits_indices[:k]

    # Sắp xếp lại K cặp này theo vị trí từ bé đến lớn
    selected_indices.sort(key=lambda x: x[1])

    # Lấy ra các ký tự ứng với K vị trí đã chọn và ghép chúng thành một số
    result = int(''.join(str(s[i]) for _, i in selected_indices))

    return result

# Đọc dữ liệu đầu vào
s = "Tinhoc95Tre68nam2023"
k = 3

# Gọi hàm và in ra kết quả
result = maximize_profit(s, k)
print(result)
