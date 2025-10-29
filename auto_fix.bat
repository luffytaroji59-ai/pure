@echo off
REM Automatic fix for ChromeDriver version issues (Windows)

echo ╔══════════════════════════════════════════════════════════════════╗
echo ║           Automatic ChromeDriver Fix                            ║
echo ╚══════════════════════════════════════════════════════════════════╝
echo.

echo [*] Step 1: Clearing ChromeDriver cache...
rmdir /s /q "%APPDATA%\undetected_chromedriver" 2>nul
rmdir /s /q ".wdm" 2>nul
echo [+] Cache cleared

echo.
echo [*] Step 2: Upgrading undetected-chromedriver...
pip install --upgrade undetected-chromedriver

echo.
echo [*] Step 3: Upgrading selenium...
pip install --upgrade selenium

echo.
echo [+] Done! Now try running: python main.py
pause
