@echo off
REM Batch file to run frontend without PowerShell execution policy issues
cd /d "%~dp0"
npm install
npm run dev
