# 🚗 Euro Trends - BMW x ISM DevOps Salary Mapping Dashboard

<div align="center">

![BMW](https://img.shields.io/badge/BMW-003087?style=for-the-badge&logo=bmw&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![React](https://img.shields.io/badge/React-18.3-61DAFB?style=for-the-badge&logo=react)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask)
![TypeScript](https://img.shields.io/badge/TypeScript-5.1-3178C6?style=for-the-badge&logo=typescript)

**A full-stack analytics platform for DevOps salary intelligence across European markets**

[Features](#-features) • [Quick Start](#-quick-start) • [Tech Stack](#-technology-stack) • [API Docs](#-api-endpoints) • [Screenshots](#-screenshots)

</div>

---

## 🎯 Project Overview

This application provides comprehensive salary analysis and forecasting for DevOps roles across Europe, developed as part of the BMW x ISM (International School of Management) field project. It processes **39,676+ real salary records** and provides actionable insights for workforce planning.

### Key Capabilities
✅ **Real-time data filtering** with Streamlit-inspired sidebar UI  
✅ **ML-powered forecasting** using scikit-learn Random Forest  
✅ **Interactive visualizations** with Plotly.js  
✅ **Multi-dimensional analysis** across countries, roles, and team setups  
✅ **Economic & legal context** for each market  
✅ **Custom data upload** supporting CSV/XLSX formats  

---

## 🚀 Features

### 📊 Five Interactive Dashboards

#### 1. **Overview Dashboard**
- Real-time metrics (filtered records, avg/min/max salary)
- Salary distribution by country (bar charts)
- Top 10 roles by average salary
- Dynamic updates based on sidebar filters

#### 2. **Salary Explorer**
- Searchable table with 39K+ records
- Real-time filtering by country, role, team setup
- Displays min/avg/max salary for each position
- Pagination support for large datasets

#### 3. **5-Year Salary Forecast**
- Machine learning predictions (2025-2030)
- Confidence intervals (upper/lower bounds)
- Filter by specific country and role
- Historical trend analysis

#### 4. **Economic Context**
- GDP per capita by country
- Cost of living indices
- Unemployment and inflation rates
- Economic indicator charts

#### 5. **Legal & Cultural Context**
- Working hours and vacation days
- Minimum wage and tax rates
- Benefits packages by country
- Regulatory compliance information

### 🎨 UI/UX Features
- **Sidebar Navigation**: Streamlit-style layout with collapsible filters
- **Multiselect Filters**: Checkbox-based selection for countries, roles, team setups
- **"Select All" / "Clear"** buttons for quick filter management
- **Global Filtering**: Sidebar filters apply across all dashboard tabs
- **Responsive Design**: Mobile-friendly layouts
- **BMW Branding**: Official color scheme (#003087) throughout

---

## 📊 Technology Stack

### Backend (Flask REST API)
```python
Flask 2.3.2          # Web framework
pandas 2.3.0         # Data processing
scikit-learn 1.7.0   # ML forecasting
plotly 6.2.0         # Chart generation
openpyxl 3.1.2       # Excel file support
Flask-CORS 4.0.0     # CORS handling
```

### Frontend (React + TypeScript)
```javascript
React 18.3.1              // UI library
TypeScript 5.1.6          // Type safety
Vite 5.0.0                // Build tool
axios 1.6.0               // HTTP client
react-plotly.js 2.6.0     // Interactive charts
plotly.js 2.27.0          // Charting engine
```

### Data Source
- **BMW Data Set for WebApp.xlsx**: 39,676 records with 25+ columns
- **Economic data**: GDP, cost of living, unemployment rates
- **Legal data**: Tax rates, working hours, benefits

---

```

### 2️⃣ Backend Setup
```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```
✅ Backend running at **http://localhost:5000**

### 3️⃣ Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
✅ Frontend running at **http://localhost:5173**

### 4️⃣ Access Application
Open browser: **http://localhost:5173**

The app will auto-load the BMW dataset (39,676 records) on startup.

---

## 📁 Project Structure

```
Euro-Trends-BMW-ISM/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── data_processor.py      # Data loading & processing
│   ├── forecasting.py         # ML forecasting models
│   ├── visualizations.py      # Chart generation
│   ├── utils.py               # Helper functions
│   ├── requirements.txt       # Python dependencies
│   └── uploads/               # User-uploaded files
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx           # Main React component
│   │   ├── App.css           # Styles (Streamlit-inspired)
│   │   └── main.tsx          # Entry point
│   ├── package.json          # Node dependencies
│   ├── vite.config.ts        # Vite configuration
│   └── tsconfig.json         # TypeScript config
│
├── RuroTrends/               # Original Streamlit version
│   ├── app.py               # Streamlit dashboard
│   └── ...
│
├── infra/
│   ├── docker-compose.yml    # Docker setup
│   ├── Dockerfile.backend    # Backend container
│   └── Dockerfile.frontend   # Frontend container
│
├── BMW Data Set for WebApp.xlsx  # Primary dataset
├── README.md                     # This file
├── LICENSE                       # MIT License
└── .gitignore                   # Git ignore rules
```

---

## 🔌 API Endpoints

### Data Management
```http
POST   /api/init              # Initialize with BMW dataset
POST   /api/upload            # Upload custom CSV/XLSX
GET    /api/status            # Check data load status
```

### Data Retrieval
```http
GET    /api/data/summary      # Dataset statistics
GET    /api/data/salaries     # All salary records
GET    /api/data/by-country   # Aggregated by country
GET    /api/data/by-role      # Aggregated by role
GET    /api/economic          # Economic indicators
GET    /api/legal             # Legal/cultural data
```

### Analysis
```http
GET    /api/forecast          # 5-year salary forecast
       ?country=Germany&role=DevOps%20Engineer
```

### Example Response
```json
{
  "total_records": 39676,
  "countries": ["Germany", "France", "UK", ...],
  "roles": ["DevOps Engineer", "Site Reliability Engineer", ...],
  "salary_stats": {
    "avg": 75000,
    "min": 35000,
    "max": 150000,
    "median": 72000,
    "std": 22000
  }
}
```

---

## � Screenshots

### Dashboard Overview
- **Sidebar Filters**: Multiselect checkboxes for countries, roles, team setups
- **Metric Cards**: Real-time statistics (filtered records, avg/min/max salary)
- **Interactive Charts**: Plotly bar charts, line charts, pie charts

### Salary Explorer
- **Data Table**: 39K+ records with sorting and filtering
- **Export Options**: Download filtered data as CSV

### Forecast Dashboard
- **ML Predictions**: Random Forest model with confidence intervals
- **5-Year Projections**: 2025-2030 salary trends
- **Scenario Analysis**: Filter by country/role combinations

---

## 🚢 Deployment Options

### Option 1: Docker Compose (Recommended)
```bash
docker-compose up -d
```
- Backend: http://localhost:5000
- Frontend: http://localhost:3000

### Option 2: Manual Deployment

#### Backend (Production)
```bash
cd backend
gunicorn --bind 0.0.0.0:5000 app:app
```

#### Frontend (Build)
```bash
cd frontend
npm run build
# Serve dist/ folder with nginx or Apache
```

### Option 3: Cloud Deployment
- **Backend**: Deploy to Heroku, AWS Lambda, Google Cloud Run
- **Frontend**: Deploy to Vercel, Netlify, AWS S3 + CloudFront
- **Database**: Use PostgreSQL or MySQL for persistent storage (optional)

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

---

## 📊 Data Schema

### Salary Data Columns
```
Role_Name, Country, Team_Setup, Salary_Min_USD, 
Salary_Avg_USD, Salary_Max_USD, Experience_Level,
Years_of_Experience, Skills, Industry, Company_Size
```

### Economic Data
```
Country, GDP_per_Capita, Cost_of_Living_Index,
Unemployment_Rate, Inflation_Rate
```

### Legal Data
```
Country, Working_Hours_per_Week, Vacation_Days,
Minimum_Wage, Tax_Rate, Benefits
```

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

**BMW x ISM Field Project Team**
- Project Lead: [Your Name]
- Institution: International School of Management (ISM)
- Partner: BMW Group

---

## 🙏 Acknowledgments

- **BMW Group** for providing the comprehensive DevOps salary dataset
- **ISM** for academic support and guidance
- **Open Source Community** for amazing tools (React, Flask, Plotly, scikit-learn)

---

## 📞 Support

For questions or issues:
- 📧 Email: [your-email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/euro-trends-bmw/issues)
- 📖 Docs: [Full Documentation](https://github.com/yourusername/euro-trends-bmw/wiki)

---

<div align="center">

**Made with ❤️ for BMW x ISM DevOps Workforce Planning**

⭐ Star this repo if you find it useful!

</div>

### Prerequisites
```bash
Python 3.13+
Node.js 16+
npm or yarn
Git
```

### 1️⃣ Clone Repository
```bash
git clone <repository-url>
cd "Euro trends BMW x ISM field project for mapping Devops roles across globe"
```

### 2. Frontend Setup
```bash
cd frontend
npm install --legacy-peer-deps
npm run dev
# Dev server starts at http://localhost:5173
```

### 3. Access Application
Open your browser to `http://localhost:5173`

## 📡 Key API Endpoints

- `GET /api/status` - Health check
- `POST /api/init` - Initialize demo data
- `POST /api/upload` - Upload salary dataset
- `GET /api/data/summary` - Get dataset summary
- `GET /api/data/salaries` - Get salary data with filters
- `POST /api/forecast` - Generate salary forecasts
- `GET /api/charts/country-salaries` - Country salary chart

## 🎨 BMW Branding

The application features BMW's signature color scheme:
- **Primary Blue**: `#003087` (BMW corporate blue)
- **Interactive elements**: BMW-branded buttons and charts

## 📁 Project Structure

```
├── backend/          # Flask REST API
├── frontend/         # React + TypeScript UI
├── infra/           # Docker configuration
└── RuroTrends/      # Original analysis scripts
```

## 🛠️ Troubleshooting

- **Backend not starting**: Ensure Python 3.13+ and all dependencies installed
- **Frontend errors**: Try `npm install --legacy-peer-deps`
- **CORS issues**: Backend includes Flask-CORS for localhost:5173

## 📜 License

MIT License - see LICENSE file for details.

## 👥 Contributors

- **ISM**: Academic research and data analysis
- **BMW**: Corporate sponsorship and requirements

---

**Built with ❤️ for BMW x ISM DevOps Workforce Planning**
