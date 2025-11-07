@echo off
echo ============================================
echo Stopping Euro Trends BMW Application
echo ============================================
echo.

echo Stopping Python (Backend)...
taskkill /F /IM python.exe /T 2>nul
if %errorlevel% == 0 (
    echo ✓ Backend stopped
) else (
    echo - Backend was not running
)

echo.
echo Stopping Node.js (Frontend)...
taskkill /F /IM node.exe /T 2>nul
if %errorlevel% == 0 (
    echo ✓ Frontend stopped
) else (
    echo - Frontend was not running
)

echo.
echo ============================================
echo Application Stopped!
echo ============================================
echo.
pause
