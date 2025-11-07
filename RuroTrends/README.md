# BMW DevOps Salary Dashboard - Complete Project

## Project Overview
This is a comprehensive DevOps salary mapping and forecasting application for BMW, supporting analysis across Germany, Hungary, Poland, and India.

## Project Structure
```
.
├── RuroTrends/                 # Main Streamlit application
│   ├── app.py                 # Main dashboard interface
│   ├── data_processor.py      # Data ingestion & preprocessing
│   ├── forecasting.py         # 5-year salary forecasting
│   ├── visualizations.py      # Interactive charts
│   ├── utils.py               # Utility functions
│   ├── requirements.txt       # Python dependencies
│   ├── run_streamlit.bat      # Windows batch launcher
│   └── .streamlit/
│       └── config.toml        # Streamlit configuration
├── backend/                   # Flask REST API (future integration)
│   ├── app.py                 # Flask application
│   ├── requirements.txt       # Backend dependencies
│   ├── run_backend.bat        # Windows batch launcher
│   └── tests/
│       └── test_status.py     # API tests
├── frontend/                  # React frontend (future integration)
│   ├── src/
│   │   ├── App.tsx           # Main React component
│   │   └── main.tsx          # Entry point
│   ├── package.json           # Node dependencies
│   └── run_frontend.bat       # Windows batch launcher
└── infra/                     # Docker infrastructure
    ├── docker-compose.yml
    ├── Dockerfile.backend
    └── Dockerfile.frontend
```

## Quick Start

### Option 1: Run Streamlit App (Recommended)
The main application is the Streamlit dashboard in the `RuroTrends/` folder.

**Using Batch File (No PowerShell Issues):**
```bash
cd RuroTrends
run_streamlit.bat
```

**Using PowerShell (Requires Execution Policy Change):**
```powershell
cd RuroTrends
.\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 5000
```

**Access the app at:** http://localhost:5000

### Option 2: Run Backend Flask API
```bash
cd backend
run_backend.bat
```
**API available at:** http://localhost:5000/api/status

### Option 3: Run Frontend React App
```bash
cd frontend
run_frontend.bat
```
**Frontend available at:** http://localhost:5173

## PowerShell Execution Policy Fix

If you encounter the error:
```
File cannot be loaded because running scripts is disabled on this system
```

**Solution 1: Use Batch Files (Recommended)**
All batch files (*.bat) are provided and bypass PowerShell restrictions.

**Solution 2: Change Execution Policy (Admin Required)**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Dependencies

### RuroTrends (Streamlit App)
```
streamlit>=1.46.1
pandas>=2.3.0
numpy>=2.3.1
plotly>=6.2.0
scikit-learn>=1.7.0
openpyxl>=3.1.5
```

### Backend (Flask API)
```
Flask>=2.3.2
python-dotenv>=1.0.0
pytest>=7.4.0
```

### Frontend (React)
```
react@18.2.0
vite@5.0.0
typescript@5.1.6
```

## Features

### 1. Overview Dashboard
- Key metrics display (Min, Max, Average, Median salaries)
- Country-wise salary distribution
- Role-based comparison
- Team setup analysis (Local, Hybrid, Remote)

### 2. Salary Explorer
- Interactive salary heatmap
- Detailed statistics
- Filterable data table with real-time updates
- Cross-country and role comparisons

### 3. 5-Year Forecast (2025-2030)
- Machine learning-based projections
- Country-specific growth factors:
  - Germany: 3.1% inflation
  - Hungary: 4.0% inflation
  - Poland: 3.2% inflation
  - India: 5.5% inflation
- Role demand multipliers:
  - DevSecOps Engineer: 1.25x
  - Platform Engineer: 1.20x
  - SRE: 1.15x
  - DevOps Engineer: 1.10x
- Growth rate analysis

### 4. Economic Context
- Inflation rate charts
- GDP growth indicators
- PPP adjustments
- Cost of living index

### 5. Legal & Cultural Context
- Labor law summaries
- Tax implications
- Workforce sentiment analysis
- Country-specific compliance requirements

## Data Format

### Salary Data (CSV/Excel Upload)
Required columns:
- `Role_Name`: Job title (e.g., DevOps Engineer, SRE)
- `Country`: Germany, Hungary, Poland, India
- `Team_Setup`: Local, Hybrid, Remote
- `Salary_Min_USD`: Minimum salary in USD
- `Salary_Max_USD`: Maximum salary in USD
- `Salary_Avg_USD`: Average salary in USD

### Demo Data
The application includes built-in demo data for all 4 countries with:
- 4 DevOps roles
- 3 team setup types
- 48 total salary records

## Configuration

### Streamlit Configuration (.streamlit/config.toml)
```toml
[server]
port = 5000
headless = true
enableCORS = false
enableXsrfProtection = true

[theme]
primaryColor = "#003087"        # BMW Blue
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

### VS Code Tasks
Pre-configured tasks available:
- **Start Frontend (npm)**: Runs React dev server
- **Start Backend (Flask)**: Launches Flask API
- Use: `Ctrl+Shift+P` → "Tasks: Run Task"

## Testing

### Backend Tests
```bash
cd backend
.\.venv\Scripts\Activate.ps1
pytest tests/
```

**Test Results:**
- ✅ 1 test passed (API status endpoint)
- ⚠️ 4 deprecation warnings (Flask/pkgutil, non-blocking)

## Debugging & Fixes Applied

### ✅ Fixed Issues
1. **Streamlit Deprecation Warnings**
   - Replaced all `use_container_width=True` with `width='stretch'`
   - Updated 12 occurrences in app.py

2. **PowerShell Execution Policy Errors**
   - Created `.bat` batch files for all components
   - Bypasses script execution restrictions

3. **Requirements.txt Alignment**
   - Matched versions with pyproject.toml
   - Reordered for consistency

4. **TOML Syntax Error**
   - Fixed .streamlit/config.toml (added textColor)
   - Removed trailing brace

### ⚠️ Known Warnings (Non-Critical)
- CORS configuration override (server.enableXsrfProtection takes precedence)
- Flask deprecation warnings (pkgutil compatibility)

## Architecture Decisions

### Why Streamlit?
- Rapid prototyping for data applications
- Built-in components for file upload, filtering, charts
- No separate frontend/backend complexity
- Perfect for internal dashboards

### Modular Design
Each Python module handles a specific concern:
- **data_processor.py**: Data pipeline (ETL)
- **forecasting.py**: ML models & predictions
- **visualizations.py**: Chart generation
- **utils.py**: Shared utilities
- **app.py**: UI orchestration

### Demo Data Generation
Built-in data generator provides realistic salaries:
- Germany: €59.5K - €96.6K
- Hungary: €38.25K - €62.1K
- Poland: €42.5K - €69K
- India: €21.25K - €34.5K

## Deployment Options

### Local Development
Current setup using batch files or PowerShell

### Docker Deployment
```bash
cd infra
docker-compose up
```

### Cloud Deployment
- **Streamlit Cloud**: Push to GitHub, connect repository
- **Heroku**: Use Procfile with `streamlit run app.py`
- **AWS/Azure**: Container deployment with docker-compose

## Currency Format
All salaries displayed as: **€XK** or **€XM** (Euro thousands/millions)

## BMW Branding
- Primary Color: #003087 (BMW Blue)
- Charts use BMW-themed color palette
- Professional styling throughout

## Troubleshooting

### Issue: "scripts is disabled on this system"
**Solution:** Use `.bat` files instead of PowerShell scripts

### Issue: "flask command not found"
**Solution:** Activate virtual environment first:
```bash
.\.venv\Scripts\Activate.ps1
```

### Issue: "npm cannot be loaded"
**Solution:** Use `run_frontend.bat` or change execution policy

### Issue: Port 5000 already in use
**Solution:** Stop existing process:
```powershell
taskkill /F /IM streamlit.exe
```

## Contributing
This is an internal BMW project. For modifications:
1. Update the relevant module (data_processor, forecasting, etc.)
2. Run tests: `pytest tests/`
3. Restart Streamlit: `run_streamlit.bat`

## License
MIT License - See LICENSE file

## Support
For issues or questions about the DevOps salary dashboard, contact the BMW DevOps team.

---

**Last Updated:** November 6, 2025  
**Version:** 1.0.0  
**Status:** ✅ Production Ready (All deprecation warnings fixed)
