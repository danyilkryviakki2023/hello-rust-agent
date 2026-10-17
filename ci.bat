@echo off
setlocal

cargo build --release
if errorlevel 1 exit /b 1

cargo test --release
if errorlevel 1 exit /b 1

if not exist dist mkdir dist
copy /Y target\release\hello.exe dist\hello.exe >nul
if errorlevel 1 exit /b 1

dist\hello.exe > ci-output.txt
if errorlevel 1 exit /b 1
findstr /C:"Hello, World!" ci-output.txt >nul
if errorlevel 1 exit /b 1
findstr /C:"2 + 3 = 5" ci-output.txt >nul
if errorlevel 1 exit /b 1
del ci-output.txt

exit /b 0