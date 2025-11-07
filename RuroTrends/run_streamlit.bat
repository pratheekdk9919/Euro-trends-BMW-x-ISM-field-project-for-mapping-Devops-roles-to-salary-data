@echo off
REM Batch file to run Streamlit app without PowerShell execution policy issues
cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run app.py --server.port 5000
