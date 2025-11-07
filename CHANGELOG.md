# Changelog

All notable changes to the Euro Trends BMW x ISM project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-07

### 🎉 Initial Release

#### Added
- **Full-Stack Dashboard**: React + TypeScript frontend with Flask backend
- **BMW Dataset Integration**: Auto-loads 39,676 salary records from BMW Data Set for WebApp.xlsx
- **5 Interactive Dashboards**:
  - Overview: Real-time metrics and salary distribution charts
  - Salary Explorer: Searchable table with 39K+ records
  - 5-Year Forecast: ML-powered salary predictions using Random Forest
  - Economic Context: GDP, cost of living, unemployment data
  - Legal & Cultural: Tax rates, working hours, benefits by country
- **Streamlit-Inspired UI**: 
  - Left sidebar with filters (countries, roles, team setups)
  - Multiselect checkboxes with "Select All" / "Clear" buttons
  - Global filtering across all dashboard tabs
- **REST API**: 15+ endpoints for data retrieval and analysis
- **Interactive Visualizations**: Plotly.js charts (bar, line, pie)
- **File Upload**: Support for CSV and XLSX custom datasets
- **Real-Time Filtering**: Dynamic updates as filters change
- **Responsive Design**: Mobile-friendly layouts

#### Backend Features
- Flask 2.3.2 REST API
- pandas for data processing (39,676 records)
- scikit-learn Random Forest forecasting
- Automatic dataset loading on startup
- CORS support for cross-origin requests
- Economic and legal data endpoints
- Salary aggregation by country and role

#### Frontend Features
- React 18.3.1 with TypeScript 5.1.6
- Vite 5.0.0 for fast builds
- Sidebar layout with multiselect filters
- 5 tabbed dashboard views
- Plotly.js interactive charts
- Real-time data filtering
- File upload with progress feedback
- BMW branding (color: #003087)

#### Data Processing
- 39,676 salary records from BMW dataset
- 25+ data fields per record
- Economic indicators for 15+ countries
- Legal/cultural data for European markets
- Automated data cleaning and validation

#### Developer Experience
- Docker Compose setup
- Batch scripts for easy startup (Windows)
- Comprehensive documentation
- Type-safe TypeScript code
- Modular Python backend
- RESTful API design

### 🔧 Technical Details

#### Dependencies
**Backend:**
- Flask 2.3.2
- pandas 2.3.0
- scikit-learn 1.7.0
- plotly 6.2.0
- openpyxl 3.1.2
- Flask-CORS 4.0.0

**Frontend:**
- React 18.3.1
- TypeScript 5.1.6
- Vite 5.0.0
- axios 1.6.0
- react-plotly.js 2.6.0
- plotly.js 2.27.0

#### Performance
- Handles 39K+ records without lag
- Real-time chart updates (<100ms)
- Efficient data aggregation
- Lazy loading for large tables

#### Browser Support
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (responsive)

---

## [Unreleased]

### Planned Features
- [ ] Export filtered data to CSV
- [ ] Advanced statistical analysis
- [ ] Role comparison tool
- [ ] Salary calculator by location
- [ ] Dark mode theme
- [ ] User authentication
- [ ] Saved filter presets
- [ ] Database persistence (PostgreSQL)
- [ ] API rate limiting
- [ ] Caching for improved performance

### Known Issues
- None reported

---

## Version History

### Version Numbering
- **MAJOR**: Incompatible API changes
- **MINOR**: New features (backward-compatible)
- **PATCH**: Bug fixes (backward-compatible)

### Release Schedule
- Major releases: Quarterly
- Minor releases: Monthly
- Patch releases: As needed

---

**For detailed commit history, see [GitHub Commits](https://github.com/yourusername/euro-trends-bmw/commits/main)**
