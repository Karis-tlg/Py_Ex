@echo off

REM Thay đổi đường dẫn đến thư mục của repository của bạn
set REPO_PATH="E:\Tin\Py_Ex"

REM Di chuyển đến thư mục của repository
cd %REPO_PATH%

REM Thêm tất cả các tệp đã thay đổi vào vùng index
git add .

REM Commit các thay đổi với thông điệp mặc định
git commit -m "Update from push_to_github.bat"

REM Đẩy các thay đổi lên GitHub
git push origin main
