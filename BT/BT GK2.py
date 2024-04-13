def main():
    n = input("Nhập dãy số, cách nhau bởi dấu cách: ").split()

    m = []
    for i in n:
        m.append(int(i))  

    k = input("Chọn điều kiện (chẵn/lẻ): ")

    t = []
    for i in m:  
        if (i % 2 == 0 and k == "chẵn") or (i % 2 != 0 and k == "lẻ"):
            t.append(i)

    tong = sum(t)
    dem = len(t)
    tb = tong / dem if dem > 0 else 0
    tb = int(tb) if tb.is_integer() else round(tb, 2)
    nho = min(t) if t else None
    to = max(t) if t else None

    print(f"""
Tổng của dãy số {k} là: {tong}
Số phần tử của dãy số {k} là: {dem}
Trung bình của dãy số {k} là: {tb}
Giá trị nhỏ nhất của dãy số {k} là: {nho}
Giá trị lớn nhất của dãy số {k} là: {to}
    """)

main()
