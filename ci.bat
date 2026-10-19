@echo off
setlocal
<<<<<<< HEAD

cargo build --release
if errorlevel 1 exit /b 1

cargo test --release
if errorlevel 1 exit /b 1

=======
cd /d "%~dp0"

echo === cargo build --release ===
cargo build --release
if errorlevel 1 exit /b 1

echo === cargo test --release ===
cargo test --release
if errorlevel 1 exit /b 1

echo === packaging into dist ===
>>>>>>> origin/develop
if not exist dist mkdir dist
copy /Y target\release\hello.exe dist\hello.exe >nul
if errorlevel 1 exit /b 1

<<<<<<< HEAD
dist\hello.exe > ci-output.txt
if errorlevel 1 exit /b 1
findstr /C:"Hello, World!" ci-output.txt >nul
if errorlevel 1 exit /b 1
findstr /C:"2 + 3 = 5" ci-output.txt >nul
if errorlevel 1 exit /b 1
del ci-output.txt

exit /b 0
=======
echo === running dist\hello.exe ===
dist\hello.exe > dist\output.txt
if errorlevel 1 exit /b 1
type dist\output.txt
findstr /C:"Hello, World!" dist\output.txt >nul
if errorlevel 1 exit /b 1

echo CI OK
exit /b 0
>>>>>>> origin/develop
