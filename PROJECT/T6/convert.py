import pandas as pd
import os

def Exel2Csv(input, output):
    os.makedirs(output, exist_ok=True)
    try:
        xls = pd.ExcelFile(input, engine='openpyxl')
    except Exception as e:
        print(f"Lỗi đọc tệp: {e}")
        return
    
    columns = {'TT': 0, 'HoVaTen': 3, 'GT': 4, 'NgaySinh': 5}
    
    for sheet in xls.sheet_names:
        try:
            df = pd.read_excel(input, sheet_name=sheet, header=None, engine='openpyxl')
            data = {}
            
            for key, idx in columns.items():
                if idx >= df.shape[1]:
                    raise ValueError(f"Cột số {idx} không tồn tại trong sheet '{sheet}'.")
                header_row = 6 if pd.notna(df.iat[6, idx]) else 7
                col_data = df.iloc[header_row + 1:, idx].reset_index(drop=True)
                header = df.iat[header_row, idx]
                data[key] = col_data
            df_final = pd.DataFrame(data)
            df_final.columns = ['TT', 'HoVaTen', 'GT', 'NgaySinh']
            df_final['HoVaTen'] = df_final['HoVaTen'].apply(lambda x: ' '.join(str(x).split()))
            df_final.dropna(subset=['TT'], inplace=True)
            df_final['NgaySinh'] = pd.to_datetime(df_final['NgaySinh'], errors='coerce').dt.strftime('%d-%m-%Y')
            df_final.reset_index(drop=True, inplace=True)
            output_csv = os.path.join(output, f"{sheet}.csv")
            df_final.to_csv(output_csv, index=False, encoding='utf-8-sig')
            print(f"Đã chuyển đổi sheet '{sheet}' thành '{output_csv}'.")
        except Exception as e:
            print(f"Lỗi trong sheet '{sheet}': {e}")

input = 'BienChe.xlsx'    
output = 'CSV'     
    
if os.path.isfile(input):
    Exel2Csv(input, output)
else:
    print(f"Lỗi: Tệp '{input}' không tồn tại.")
