# Complete Setup Guide for BMW DevOps Salary Dashboard

## 🎯 Overview
This guide ensures all required extensions, programming languages, and dependencies are properly installed for the Euro Trends BMW × ISM DevOps Salary Dashboard project.

---

## 📋 Prerequisites

### 1. **Programming Languages**

#### Python 3.13+
- **Check Installation:**
  ```powershell
  python --version
  ```
- **Expected Output:** `Python 3.13.4` or higher
- **Download:** https://www.python.org/downloads/
- **Installation Notes:** 
  - ✅ Select "Add Python to PATH" during installation
  - ✅ Install pip (included by default)

#### Node.js 18+ and npm
- **Check Installation:**
  ```powershell
  node --version
  npm --version
  ```
- **Expected Output:** `v18.x.x` or higher for Node, `9.x.x` or higher for npm
- **Download:** https://nodejs.org/
- **Installation Notes:** npm is included with Node.js

---

## 🔧 VS Code Extensions

### Required Extensions

1. **Python** (`ms-python.python`)
   - Official Python language support
   - Features: IntelliSense, linting, debugging, Jupyter support
   - **Install Command:**
     ```
     code --install-extension ms-python.python
     ```

2. **Pylance** (`ms-python.vscode-pylance`)
   - Fast Python language server
   - Features: Type checking, auto-imports, better IntelliSense
   - **Install Command:**
     ```
     code --install-extension ms-python.vscode-pylance
     ```

3. **ESLint** (`dbaeumer.vscode-eslint`)
   - JavaScript/TypeScript linting
   - **Install Command:**
     ```
     code --install-extension dbaeumer.vscode-eslint
     ```

4. **Prettier** (`esbenp.prettier-vscode`)
   - Code formatter for JavaScript, TypeScript, CSS, HTML
   - **Install Command:**
     ```
     code --install-extension esbenp.prettier-vscode
     ```

5. **ES7+ React/Redux/React-Native snippets** (`dsznajder.es7-react-js-snippets`)
   - React code snippets
   - **Install Command:**
     ```
     code --install-extension dsznajder.es7-react-js-snippets
     ```

### Recommended Extensions

6. **GitLens** (`eamodio.gitlens`)
   - Enhanced Git integration
   - **Install Command:**
     ```
     code --install-extension eamodio.gitlens
     ```

7. **Thunder Client** (`rangav.vscode-thunder-client`)
   - REST API testing (alternative to Postman)
   - **Install Command:**
     ```
     code --install-extension rangav.vscode-thunder-client
     ```

---

## 📦 Backend Setup (Python/Flask)

### 1. Create Virtual Environment
```powershell
cd backend
python -m venv .venv
```

### 2. Activate Virtual Environment
```powershell
# PowerShell
.\.venv\Scripts\Activate.ps1

# If you get execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Verify Installation
```powershell
pip list
```

**Expected Packages:**
- Flask==2.3.2
- Flask-CORS==4.0.0
- pandas==2.3.0
- numpy==2.3.1
- scikit-learn==1.7.0
- plotly==6.2.0
- openpyxl==3.1.5

---

## 🎨 Frontend Setup (React/TypeScript)

### 1. Navigate to Frontend
```powershell
cd frontend
```

### 2. Install Dependencies
```powershell
npm install --legacy-peer-deps
```

### 3. Verify Installation
```powershell
npm list --depth=0
```

**Expected Packages:**
- react@18.3.1
- react-dom@18.3.1
- typescript@5.1.6
- vite@5.0.0
- axios@1.6.0
- plotly.js@2.27.0
- react-plotly.js@2.6.0
- @types/react@18.3.20
- @types/react-dom@18.3.6
- @types/react-plotly.js@2.6.3

---

## 🚀 Running the Application

### Option 1: Using Batch Files (Easiest)
```powershell
# From project root
.\START_APPLICATION.bat
```

This will:
- Start backend on http://localhost:5000
- Start frontend on http://localhost:5173
- Open in separate terminal windows

### Option 2: Using VS Code Tasks
1. Press `Ctrl+Shift+P`
2. Type "Run Task"
3. Select:
   - `Start Backend (Flask)` 
   - `Start Frontend (npm)`

### Option 3: Manual Start
**Terminal 1 - Backend:**
```powershell
cd backend
python app.py
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm run dev
```

---

## 🧪 Testing the Setup

### 1. Backend Health Check
```powershell
# Test API status
Invoke-RestMethod -Uri "http://localhost:5000/api/status" | ConvertTo-Json
```

**Expected Response:**
```json
{
  "status": "ok",
  "data_loaded": true,
  "total_records": 39676
}
```

### 2. Frontend Access
- Open browser: http://localhost:5173
- You should see the BMW DevOps Dashboard
- Data should load automatically (39,676 records)

### 3. All Features Test
Navigate through tabs:
- ✅ **Overview** - Metrics cards, country/role charts
- ✅ **Salary Explorer** - Filterable data table
- ✅ **5-Year Forecast** - ML salary predictions
- ✅ **Economic Context** - GDP, cost of living, unemployment
- ✅ **Legal & Cultural** - Work regulations, tax rates, benefits

---

## 🐛 Troubleshooting

### Python Issues

**Problem:** `python: command not found`
```powershell
# Solution: Add Python to PATH
[System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Python313", [System.EnvironmentVariableTarget]::User)
```

**Problem:** Virtual environment won't activate
```powershell
# Solution: Change execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Problem:** Flask won't start - sklearn error
```powershell
# Solution: Already fixed in app.py (debug=False, use_reloader=False)
```

### Node.js Issues

**Problem:** `npm install` fails with peer dependency errors
```powershell
# Solution: Use legacy peer deps flag
npm install --legacy-peer-deps
```

**Problem:** `npm run dev` fails
```powershell
# Solution: Delete node_modules and reinstall
Remove-Item -Recurse -Force node_modules
npm install --legacy-peer-deps
```

### Backend Issues

**Problem:** Backend returns "No data loaded"
```powershell
# Solution: Call init endpoint
Invoke-RestMethod -Uri "http://localhost:5000/api/init" -Method Post
```

**Problem:** Can't find BMW dataset
```powershell
# Solution: Verify file exists
Get-Item "../BMW Data Set for WebApp.xlsx"
```

### Frontend Issues

**Problem:** CORS errors in browser console
```powershell
# Solution: Ensure Flask-CORS is installed and backend is running
pip install Flask-CORS
```

**Problem:** Data doesn't auto-load
```powershell
# Solution: Already fixed - frontend now auto-loads when backend has data
```

---

## 📊 Dataset Information

### BMW Data Set for WebApp.xlsx
- **Location:** Project root folder
- **Records:** 39,676 salary entries
- **Countries:** India, Germany, Poland, Hungary
- **Roles:** DevOps Engineer, Senior DevOps Engineer, Lead DevOps Engineer, etc.
- **Auto-Loading:** Backend loads this dataset automatically on startup

---

## 🔒 Security Notes

### PowerShell Execution Policy
The batch files bypass execution policy safely:
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -Command "..."
```

### CORS Configuration
Backend allows requests from:
- http://localhost:5173 (frontend development)
- http://localhost:3000 (alternative port)

### Production Deployment
Before deploying to production:
1. Set `FLASK_ENV=production`
2. Update CORS origins to actual domain
3. Add authentication/authorization
4. Use environment variables for secrets

---

## 📝 File Structure Verification

Run this command to verify all files are in place:
```powershell
Get-ChildItem -Recurse -File | Select-Object FullName | Format-Table -AutoSize
```

### Critical Files Checklist
- [ ] `backend/app.py` - Main Flask application
- [ ] `backend/requirements.txt` - Python dependencies
- [ ] `backend/data_processor.py` - Data processing module
- [ ] `backend/forecasting.py` - ML forecasting module
- [ ] `backend/visualizations.py` - Chart generation module
- [ ] `frontend/src/App.tsx` - Main React component
- [ ] `frontend/src/App.css` - BMW branding styles
- [ ] `frontend/package.json` - Node dependencies
- [ ] `BMW Data Set for WebApp.xlsx` - Dataset (root folder)
- [ ] `START_APPLICATION.bat` - Easy startup script
- [ ] `STOP_APPLICATION.bat` - Easy shutdown script

---

## ✅ Success Criteria

Your setup is complete when:
1. ✅ Backend starts without errors on port 5000
2. ✅ Frontend starts without errors on port 5173
3. ✅ Browser shows dashboard with BMW branding
4. ✅ Dashboard displays 39,676 records automatically
5. ✅ All 5 tabs work (Overview, Explorer, Forecast, Economic, Legal)
6. ✅ Charts render correctly (Plotly visualizations)
7. ✅ Filters work in Salary Explorer
8. ✅ Forecast generates predictions
9. ✅ Economic and Legal data displays

---

## 📞 Support

If you encounter issues:
1. Check this guide's troubleshooting section
2. Review `README.md` for additional context
3. Check `INTEGRATION_COMPLETE.md` for technical details
4. Verify all extensions are installed in VS Code
5. Ensure Python 3.13+ and Node.js 18+ are installed

---

## 🎉 Next Steps

Once setup is complete:
1. Explore all dashboard features
2. Test file upload functionality
3. Generate forecasts with different filters
4. Review economic and legal data by country
5. Prepare for GitHub deployment

**Happy Coding! 🚀**
