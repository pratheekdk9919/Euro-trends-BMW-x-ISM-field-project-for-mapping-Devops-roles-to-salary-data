# 🚗 Euro Trends - BMW x ISM DevOps Salary Mapping Dashboard

<div align="center">

![BMW](https://img.shields.io/badge/BMW-003087?style=for-the-badge&logo=bmw&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![React](https://img.shields.io/badge/React-18.3-61DAFB?style=for-the-badge&logo=react)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask)
![TypeScript](https://img.shields.io/badge/TypeScript-5.1-3178C6?style=for-the-badge&logo=typescript)

![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Code Quality](https://img.shields.io/badge/Code%20Quality-Professional-brightgreen?style=for-the-badge)
![German Market](https://img.shields.io/badge/Focus-German%20Market-red?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0iI0ZGQ0UwMCIvPjwvc3ZnPg==)

**A full-stack analytics platform for DevOps salary intelligence across European markets**  
*Entwickelt in Zusammenarbeit mit BMW Group und International School of Management*

[Features](#-features) • [Quick Start](#-quick-start) • [Tech Stack](#-technology-stack) • [API Docs](#-api-endpoints) • [Deployment](#-deployment-options)

</div>

---

## 🌍 Deutsche Zusammenfassung / German Summary

Diese Anwendung bietet eine umfassende Gehaltsanalyse und -prognose für DevOps-Rollen in Europa, entwickelt im Rahmen des BMW x ISM Feldprojekts. Die Plattform verarbeitet **39.676+ echte Gehaltsdatensätze** und bietet fundierte Erkenntnisse für die Personalplanung.

**Kernfunktionen:**
- 🎯 Echtzeit-Datenfilterung nach Ländern, Rollen und Team-Setups
- 🤖 ML-gestützte 5-Jahres-Prognosen (2025-2030)
- 📊 Interaktive Dashboards mit Plotly.js
- 🌍 Wirtschaftliche und rechtliche Kontextinformationen für deutsche und europäische Märkte
- 💼 Spezieller Fokus auf den deutschen DevOps-Arbeitsmarkt

---

## 🎯 Project Overview

This application provides comprehensive salary analysis and forecasting for DevOps roles across Europe, developed as part of the BMW x ISM (International School of Management) field project. It processes **39,676+ real salary records** and provides actionable insights for workforce planning.

### Professional Use Cases

This platform is designed for:
- 🏢 **HR Professionals & Recruiters**: Make data-driven compensation decisions
- 💼 **Hiring Managers**: Benchmark salaries against market standards
- 📊 **Workforce Analysts**: Identify trends and plan budgets
- 🎓 **Job Seekers**: Research competitive salary ranges for DevOps roles
- 📈 **Business Leaders**: Understand European DevOps talent market dynamics

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

## 📈 Data Quality & Methodology

### Dataset Specifications
- **Total Records**: 39,676 validated salary entries
- **Geographic Coverage**: Germany, France, UK, Netherlands, Switzerland, and more
- **Data Points**: 25+ attributes per record including role, experience, skills, and compensation
- **Time Period**: Current market data with historical trends
- **Source**: BMW Group's comprehensive DevOps salary research

### Analysis Methodology
- **Machine Learning**: Random Forest regression with confidence intervals
- **Statistical Methods**: Robust aggregation and outlier detection
- **Validation**: Cross-validation and testing for model accuracy
- **Updates**: Regular data refresh cycles for market relevance

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

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Pratheek DK & BMW x ISM Field Project Team

---

## 👥 Authors

**BMW x ISM Field Project Team**
- Project Lead: Pratheek DK
- Institution: International School of Management (ISM)
- Partner: BMW Group
- Repository: [pratheekdk9919](https://github.com/pratheekdk9919)

---

## 🙏 Acknowledgments

- **BMW Group** for providing the comprehensive DevOps salary dataset and supporting this research
- **International School of Management (ISM)** for academic guidance and institutional support
- **German Tech Industry** for insights into the European DevOps market landscape
- **Open Source Community** for exceptional tools: React, Flask, Plotly, scikit-learn, TypeScript, and Vite
- **European DevOps Community** for contributing to the understanding of market trends

### Special Recognition

This project demonstrates the application of data science and full-stack development principles to solve real-world HR and workforce planning challenges in the European tech industry, with particular focus on the German market.

---

## 📞 Support

For questions or issues:
- 🐛 Issues: [GitHub Issues](https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data/issues)
- 📖 Repository: [GitHub Repository](https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data)

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
git clone https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data.git
cd Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data
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
