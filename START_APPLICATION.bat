@echo off
echo ============================================
echo Starting Euro Trends BMW Application
echo ============================================
echo.

echo [1/2] Starting Backend (Flask)...
start "Backend - Flask" cmd /k "cd /d "%~dp0backend" && python app.py"
timeout /t 3 /nobreak > nul

echo [2/2] Starting Frontend (React + Vite)...
start "Frontend - React" cmd /k "cd /d "%~dp0frontend" && npm run dev"
timeout /t 2 /nobreak > nul

echo.
echo ============================================
echo Application Started!
echo ============================================
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:5173
echo.
echo Press any key to close this window...
pause > nul
