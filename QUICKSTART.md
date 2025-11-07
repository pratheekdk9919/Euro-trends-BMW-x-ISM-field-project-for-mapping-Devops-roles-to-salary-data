# 🚀 First-Time Setup Guide

Welcome! This guide will help you set up the Euro Trends BMW x ISM Dashboard from scratch.

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Python 3.11 or higher** ([Download](https://www.python.org/downloads/))
- [ ] **Node.js 18.x or higher** ([Download](https://nodejs.org/))
- [ ] **npm** (comes with Node.js) or **yarn**
- [ ] **Git** ([Download](https://git-scm.com/downloads))
- [ ] At least **2GB free disk space**
- [ ] Internet connection (for package installation)

**Optional (for Docker deployment):**
- [ ] **Docker Desktop** ([Download](https://www.docker.com/products/docker-desktop/))

---

## 🛠️ Step-by-Step Installation

### Step 1: Clone the Repository

```bash
# Using HTTPS
git clone https://github.com/yourusername/euro-trends-bmw.git
cd euro-trends-bmw

# Or using SSH
git clone git@github.com:yourusername/euro-trends-bmw.git
cd euro-trends-bmw
```

### Step 2: Backend Setup (Flask API)

#### Windows PowerShell
```powershell
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
python -c "import flask; print(f'Flask {flask.__version__} installed successfully')"
```

#### Windows Command Prompt
```cmd
cd backend
python -m venv venv
venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
```

#### macOS/Linux
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### Troubleshooting Backend Installation

**Problem: Python command not found**
```bash
# Windows: Check if Python is in PATH
python --version

# If not found, add Python to PATH or use:
py --version

# macOS/Linux: Use python3
python3 --version
```

**Problem: pip install fails**
```bash
# Clear pip cache
pip cache purge

# Install with verbose logging
pip install -v -r requirements.txt

# Install one package at a time to identify issue
pip install flask
pip install pandas
# ... etc
```

**Problem: Permission denied (Windows)**
```powershell
# Run PowerShell as Administrator
# Or change execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Problem: Missing build tools (Windows)**
```
# Install Microsoft C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Select: "Desktop development with C++"
```

### Step 3: Frontend Setup (React + TypeScript)

```bash
# Navigate to frontend (from project root)
cd ../frontend

# Install dependencies
npm install

# Or using yarn
yarn install

# Verify installation
npm list react
```

#### Troubleshooting Frontend Installation

**Problem: npm command not found**
```bash
# Verify Node.js installation
node --version
npm --version

# Reinstall Node.js if needed
# Download from: https://nodejs.org/
```

**Problem: npm install fails**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json  # macOS/Linux
rmdir /s /q node_modules & del package-lock.json  # Windows

# Reinstall
npm install

# Try using legacy peer deps
npm install --legacy-peer-deps
```

**Problem: EACCES permission error (macOS/Linux)**
```bash
# Don't use sudo! Instead, fix npm permissions:
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Step 4: Verify Data Files

```bash
# Return to project root
cd ..

# Check if BMW dataset exists
ls "BMW Data Set for WebApp.xlsx"

# Windows PowerShell
Test-Path "BMW Data Set for WebApp.xlsx"
```

**If data file is missing:**
- The backend will auto-load this file on startup
- Ensure the file is in the project root directory
- File should be exactly named: `BMW Data Set for WebApp.xlsx`

### Step 5: Run the Applications

#### Option 1: Using Batch Scripts (Windows)

**Start Backend:**
```cmd
# Double-click backend/run_backend.bat
# Or in command prompt:
cd backend
run_backend.bat
```

**Start Frontend:**
```cmd
# Double-click frontend/run_frontend.bat
# Or in command prompt:
cd frontend
run_frontend.bat
```

#### Option 2: Manual Start (All Platforms)

**Terminal 1 - Backend:**
```bash
cd backend
# Activate virtual environment first!
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\Activate.ps1  # Windows PowerShell

# Start Flask
flask run --host=0.0.0.0 --port=5000

# Or using Python
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

#### Option 3: Using Tasks in VS Code

1. Open Command Palette: `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. Type: "Tasks: Run Task"
3. Select: "Start Backend (Flask)"
4. Repeat for "Start Frontend (npm)"

### Step 6: Access the Dashboard

Open your browser and navigate to:

- **Frontend UI**: http://localhost:5174
- **Backend API**: http://localhost:5000
- **API Status**: http://localhost:5000/api/status

You should see:
- ✅ Frontend loading with Streamlit-style sidebar
- ✅ Backend serving data from BMW dataset
- ✅ 39,676 records loaded automatically

---

## 🧪 Verify Installation

Run the verification script:

```bash
# From project root
python verify_setup.py
```

Expected output:
```
✅ Python 3.11+ installed
✅ Node.js 18+ installed
✅ Backend dependencies installed
✅ Frontend dependencies installed
✅ BMW dataset found
✅ Backend server running on port 5000
✅ Frontend server running on port 5174
```

---

## 🎨 Quick Tour

### 1. Dashboard Overview
- Navigate to http://localhost:5174
- You'll see 5 tabs: Overview, Explorer, Forecast, Economic, Legal

### 2. Upload Data
- Click "Upload Data" in the sidebar
- Select the BMW dataset Excel file
- Data loads automatically (39,676 records)

### 3. Filter Data
- Use Country multiselect in sidebar
- Use Role multiselect to filter roles
- Changes apply to all tabs dynamically

### 4. Explore Dashboards
- **Overview**: Key metrics and summary statistics
- **Explorer**: Detailed data table and visualizations
- **Forecast**: Salary predictions using machine learning
- **Economic**: Economic indicators by country
- **Legal**: Legal framework and regulations

---

## 🐳 Docker Setup (Alternative)

If you prefer Docker:

```bash
# From project root
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Access points:
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

---

## 📁 Project Structure

```
euro-trends-bmw/
├── backend/              # Flask API
│   ├── app.py           # Main application
│   ├── requirements.txt # Python dependencies
│   └── venv/            # Virtual environment (created by you)
├── frontend/            # React UI
│   ├── src/             # Source code
│   ├── package.json     # Node dependencies
│   └── node_modules/    # Packages (created by npm install)
├── infra/               # Docker configs
├── BMW Data Set.xlsx    # Main dataset
├── README.md            # Project documentation
└── verify_setup.py      # Setup verification script
```

---

## 🔧 Configuration

### Backend Configuration

Create `backend/.env` (optional):
```bash
FLASK_ENV=development
FLASK_APP=app.py
FLASK_DEBUG=1
MAX_CONTENT_LENGTH=52428800
CORS_ORIGINS=http://localhost:5174
```

### Frontend Configuration

Create `frontend/.env` (optional):
```bash
VITE_API_URL=http://localhost:5000/api
VITE_ENABLE_DEBUG=true
```

---

## 🚨 Common Issues & Solutions

### Port Already in Use

**Backend (Port 5000):**
```bash
# Find process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :5000
kill -9 <PID>

# Or use a different port:
flask run --port=5001
```

**Frontend (Port 5174):**
```bash
# Vite will automatically try next available port
# Or specify in vite.config.ts:
export default defineConfig({
  server: { port: 3000 }
})
```

### CORS Errors

If you see CORS errors in browser console:

```python
# backend/app.py
from flask_cors import CORS

# Allow your frontend origin
CORS(app, origins=['http://localhost:5174'])
```

### Module Not Found

**Backend:**
```bash
# Ensure virtual environment is activated
# Check with:
pip list

# Reinstall specific package
pip install flask --upgrade
```

**Frontend:**
```bash
# Reinstall node_modules
rm -rf node_modules package-lock.json
npm install
```

### Data Not Loading

1. **Check file location**: `BMW Data Set for WebApp.xlsx` in project root
2. **Check backend logs**: Look for errors in terminal running Flask
3. **Verify API**: Visit http://localhost:5000/api/status
4. **Check file permissions**: Ensure read access to Excel file

### Slow Performance

```bash
# Backend: Reduce data in memory
# frontend/App.tsx: Enable pagination/virtualization

# Or increase system resources:
# Close unnecessary applications
# Allocate more RAM to Docker (if using Docker)
```

---

## 🔄 Updating the Project

```bash
# Pull latest changes
git pull origin main

# Update backend dependencies
cd backend
pip install --upgrade -r requirements.txt

# Update frontend dependencies
cd ../frontend
npm install

# Restart services
```

---

## 📚 Next Steps

Now that setup is complete:

1. **Read the Documentation**: Check `README.md` for features
2. **Explore the API**: See `README.md` API section for endpoints
3. **Customize**: Edit `frontend/src/App.tsx` for UI changes
4. **Deploy**: See `DEPLOYMENT.md` for production deployment
5. **Contribute**: Read `CONTRIBUTING.md` to contribute code

---

## 🆘 Getting Help

**Still having issues?**

1. **Check existing issues**: [GitHub Issues](https://github.com/yourusername/euro-trends-bmw/issues)
2. **Search documentation**: README.md, DEPLOYMENT.md, CONTRIBUTING.md
3. **Ask for help**: Open a new issue with:
   - Operating system and version
   - Python/Node.js versions
   - Complete error message
   - Steps to reproduce

**Useful debugging commands:**
```bash
# Check versions
python --version
node --version
npm --version
pip list
npm list

# Check running processes
# Windows:
netstat -ano | findstr :5000
netstat -ano | findstr :5174

# macOS/Linux:
lsof -i :5000
lsof -i :5174
```

---

## ✅ Success Checklist

After setup, verify:

- [ ] Backend running on http://localhost:5000
- [ ] Frontend running on http://localhost:5174
- [ ] API returns data: http://localhost:5000/api/status
- [ ] Dashboard loads in browser
- [ ] Can filter by country and role
- [ ] All 5 tabs accessible (Overview, Explorer, Forecast, Economic, Legal)
- [ ] Data displays correctly (39,676 records)

**Congratulations! 🎉 You're ready to use the Euro Trends BMW x ISM Dashboard!**

---

**Need more help? Contact: your-email@example.com**
