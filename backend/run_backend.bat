@echo off
REM Batch file to run Flask backend without PowerShell execution policy issues
cd /d "%~dp0"
call .venv\Scripts\activate.bat
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
