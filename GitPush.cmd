@echo off

set REPO_PATH="E:\Tin\Py_Ex"

cd %REPO_PATH%

git add .

git commit -m "Update from push_to_github.bat"

git push -u origin main
