@echo off
setlocal
cd /d "%~dp0"

echo === cargo build --release ===
cargo build --release
if errorlevel 1 exit /b 1

echo === cargo test --release ===
cargo test --release
if errorlevel 1 exit /b 1

echo === packaging into dist ===
if not exist dist mkdir dist
copy /Y target\release\hello.exe dist\hello.exe >nul
if errorlevel 1 exit /b 1

echo === running dist\hello.exe ===
dist\hello.exe > dist\output.txt
if errorlevel 1 exit /b 1
type dist\output.txt
findstr /C:"Hello, World!" dist\output.txt >nul
if errorlevel 1 exit /b 1

echo CI OK
exit /b 0
