def thí_sinh_thang_thứ_nhiều_nhất(khán_giả):
    bình_chọn = {}
    for báo_danh in khán_giả:
        if báo_danh in bình_chọn:
            bình_chọn[báo_danh] += 1
        else:
            bình_chọn[báo_danh] = 1

    max_số_bình_chọn = max(bình_chọn.values())
    thí_sinh_thắng = [k for k, v in bình_chọn.items() if v == max_số_bình_chọn]

    return sorted(thí_sinh_thắng)

# Đọc dữ liệu từ file input
with open("THANTUONG.INP", "r") as f:
    n = int(f.readline())
    khán_giả = [int(f.readline()) for _ in range(n)]


for thí_sinh in thí_sinh_thang_thứ_nhiều_nhất(khán_giả):
    print(str(thí_sinh) + "\n")

        
# Tìm và in ra thí sinh được bình chọn nhiều nhất
'''
with open("THANTUONG.OUT", "w") as f:
    for thí_sinh in thí_sinh_thang_thứ_nhiều_nhất(khán_giả):
        f.write(str(thí_sinh) + "\n")
'''
