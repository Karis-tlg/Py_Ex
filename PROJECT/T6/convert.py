import pandas as pd
from pathlib import Path
import os

def excel_to_csv(input_path: str, output_dir: str):
    """
    Chuyển đổi tất cả các sheet trong tệp Excel thành các tệp CSV riêng biệt với các cột được chọn.

    :param input_path: Đường dẫn tới tệp Excel đầu vào.
    :param output_dir: Thư mục đích để lưu các tệp CSV.
    """
    input_file = Path(input_path)
    output_directory = Path(output_dir)
    
    if not input_file.is_file():
        print(f"Lỗi: Tệp '{input_file}' không tồn tại.")
        return
    
    output_directory.mkdir(parents=True, exist_ok=True)
    
    try:
        xls = pd.ExcelFile(input_file, engine='openpyxl')
    except Exception as e:
        print(f"Lỗi đọc tệp Excel: {e}")
        return
    
    # Định nghĩa các cột dựa trên chỉ số
    COLUMN_MAPPING = {
        'TT': 0,
        'HoVaTen': 2,
        'GT': 3,
        'Ngay': 4,
        'Thang': 5,
        'Nam': 6
    }
    
    for sheet_name in xls.sheet_names:
        try:
            df = pd.read_excel(
                input_file,
                sheet_name=sheet_name,
                header=None,
                engine='openpyxl',
                skiprows=6  # Bỏ qua 6 dòng đầu
            )
            
            # Chọn các cột cần thiết
            df = df.iloc[:, list(COLUMN_MAPPING.values())]
            df.columns = COLUMN_MAPPING.keys()
            
            # Loại bỏ các hàng hoàn toàn rỗng
            df.dropna(how='all', inplace=True)
            
            # Xử lý 'TT' - chuyển thành integer và loại bỏ phần thập phân nếu có
            df['TT'] = pd.to_numeric(df['TT'], errors='coerce').astype('Int64')
            
            # Xử lý 'HoVaTen' - loại bỏ khoảng trắng thừa
            df['HoVaTen'] = df['HoVaTen'].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
            
            # Xử lý 'GT' - loại bỏ khoảng trắng thừa
            df['GT'] = df['GT'].astype(str).str.strip()
            
            # Hàm để xử lý 'NgaySinh'
            def parse_ngay_sinh(row):
                ngay = row['Ngay']
                thang = row['Thang']
                nam = row['Nam']
                
                if pd.isnull(ngay):
                    return pd.NaT
                
                # Kiểm tra nếu 'Ngay' là kiểu datetime
                if isinstance(ngay, pd.Timestamp):
                    return ngay.strftime('%d-%m-%Y')
                
                # Nếu 'Ngay' là số, xử lý như ngày, tháng, năm
                try:
                    ngay = int(ngay)
                    thang = int(thang)
                    nam = int(nam)
                    return pd.Timestamp(day=ngay, month=thang, year=nam).strftime('%d-%m-%Y')
                except Exception:
                    return pd.NaT
            
            # Áp dụng hàm xử lý 'NgaySinh' cho từng hàng
            df['NgaySinh'] = df.apply(parse_ngay_sinh, axis=1)
            
            # Loại bỏ các hàng thiếu 'TT'
            df.dropna(subset=['TT'], inplace=True)
            
            # Chuyển 'TT' về kiểu integer
            df['TT'] = df['TT'].astype(int)
            
            # Reset chỉ số
            df.reset_index(drop=True, inplace=True)
            
            # Chọn chỉ các cột cần thiết để xuất
            df_final = df[['TT', 'HoVaTen', 'GT', 'NgaySinh']]
            
            # Đường dẫn tệp CSV đầu ra
            output_csv = output_directory / f"{sheet_name}.csv"
            
            # Ghi DataFrame ra tệp CSV
            df_final.to_csv(output_csv, index=False, encoding='utf-8-sig')
            print(f"Đã chuyển đổi sheet '{sheet_name}' thành '{output_csv}'.")
        
        except Exception as e:
            print(f"Lỗi trong sheet '{sheet_name}': {e}")

if __name__ == "__main__":
    INPUT_FILE = 'BienChe2022.xlsx'
    OUTPUT_FOLDER = 'CSV2022'
    excel_to_csv(INPUT_FILE, OUTPUT_FOLDER)
