import pandas as pd
from pathlib import Path
import os
from datetime import datetime

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
                skiprows=6
            )
            
            df = df.iloc[:, list(COLUMN_MAPPING.values())]
            df.columns = COLUMN_MAPPING.keys()
            df.dropna(how='all', inplace=True)
            df['TT'] = pd.to_numeric(df['TT'], errors='coerce').astype('Int64')
            df['HoVaTen'] = df['HoVaTen'].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)
            df['GT'] = df['GT'].astype(str).str.strip()
            
            def parse_ngay_sinh(row):
                ngay, thang, nam = row['Ngay'], row['Thang'], row['Nam']
                
                # Kiểm tra nếu giá trị NaN và giữ nguyên thay vì thay thế bằng 1900
                if pd.isnull(ngay) or pd.isnull(thang) or pd.isnull(nam):
                    return ""
                
                try:
                    if isinstance(ngay, (pd.Timestamp, datetime)):
                        ngay, thang, nam = ngay.day, ngay.month, ngay.year
                    elif isinstance(ngay, str) and ngay.strip().isdigit():
                        ngay = int(ngay.strip())
                    if isinstance(thang, float):
                        thang = int(thang)
                    if isinstance(nam, float):
                        nam = int(nam)
                    
                    # Đổi năm 1900 thành 2007 nếu phát hiện lỗi
                    if nam == 1900:
                        nam = 2007
                    
                    return f"{ngay:02d}-{thang:02d}-{nam}"
                except (ValueError, TypeError):
                    return ""
            
            df['NgaySinh'] = df.apply(parse_ngay_sinh, axis=1)
            df.dropna(subset=['TT'], inplace=True)
            df['TT'] = df['TT'].astype(int)
            df.reset_index(drop=True, inplace=True)
            df_final = df[['TT', 'HoVaTen', 'GT', 'NgaySinh']]
            
            output_csv = output_directory / f"{sheet_name}.csv"
            df_final.to_csv(output_csv, index=False, encoding='utf-8-sig')
            print(f"Đã chuyển đổi sheet '{sheet_name}' thành '{output_csv}'.")
        
        except Exception as e:
            print(f"Lỗi trong sheet '{sheet_name}': {e}")

if __name__ == "__main__":
    INPUT_FILE = 'BIenChe2022.xlsx'
    OUTPUT_FOLDER = 'CSV2022'
    excel_to_csv(INPUT_FILE, OUTPUT_FOLDER)
