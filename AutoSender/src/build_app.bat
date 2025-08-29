@echo off
setlocal

echo === WhatsApp AutoSender - EXE Builder ===
where pyinstaller >nul 2>&1
if errorlevel 1 (
  echo Installing PyInstaller...
  python -m pip install --upgrade pip
  python -m pip install pyinstaller
)

REM Clean previous builds (optional)
if exist build rd /s /q build
if exist dist rd /s /q dist
if exist auto_sender_gui.spec del /q auto_sender_gui.spec

echo.
echo Building (onefile, no console)...
if exist icon.ico (
  pyinstaller --onefile --noconsole --icon=icon.ico src/auto_sender_gui.py
) else (
  pyinstaller --onefile --noconsole src/auto_sender_gui.py
)

echo.
echo ✅ Build complete!
echo Find your app here: dist\auto_sender_gui.exe
echo.
pause
endlocal
