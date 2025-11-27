# 🏗️ System Architecture

## Overview

Euro Trends is a full-stack analytics platform designed with a modern, scalable architecture separating concerns between data processing, business logic, and presentation layers.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend Layer                        │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  React 18.3 + TypeScript 5.1 + Vite 5.0              │ │
│  │  • Dashboard Components                                │ │
│  │  • Interactive Charts (Plotly.js)                     │ │
│  │  • State Management (React Hooks)                     │ │
│  │  • Responsive UI (CSS Grid/Flexbox)                   │ │
│  └────────────────────────────────────────────────────────┘ │
│                           ↕ HTTP/REST                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                        Backend Layer                         │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Flask 2.3 REST API + Flask-CORS                      │ │
│  │  • RESTful Endpoints                                   │ │
│  │  • Request Validation                                  │ │
│  │  • Error Handling                                      │ │
│  │  • CORS Configuration                                  │ │
│  └────────────────────────────────────────────────────────┘ │
│                              ↓                               │
│  ┌─────────────────┬──────────────────┬──────────────────┐ │
│  │ Data Processor  │   Forecasting    │  Visualizations  │ │
│  │  • Data Loading │   • Random Forest│   • Chart Gen    │ │
│  │  • Cleaning     │   • Predictions  │   • Plotly API   │ │
│  │  • Aggregation  │   • Validation   │   • JSON Export  │ │
│  └─────────────────┴──────────────────┴──────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                        Data Layer                            │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  BMW Dataset (Excel)                                   │ │
│  │  • 39,676 salary records                              │ │
│  │  • 25+ attributes per record                          │ │
│  │  • Economic indicators                                 │ │
│  │  • Legal/cultural context                             │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Frontend Technologies
- **React 18.3**: Modern UI library with hooks and functional components
- **TypeScript 5.1**: Type-safe JavaScript for improved code quality
- **Vite 5.0**: Fast build tool and dev server
- **Plotly.js 2.27**: Interactive, publication-quality charts
- **Axios 1.6**: HTTP client for API communication

### Backend Technologies
- **Flask 2.3**: Lightweight Python web framework
- **pandas 2.3**: Data manipulation and analysis
- **scikit-learn 1.7**: Machine learning for salary forecasting
- **Plotly 6.2**: Server-side chart generation
- **openpyxl 3.1**: Excel file processing

## Component Architecture

### Backend Components

#### 1. Data Processor (`data_processor.py`)
- Loads dataset from Excel
- Cleans and validates data
- Handles missing values and outliers
- Provides aggregation functions
- Supports custom data uploads

#### 2. Forecasting Engine (`forecasting.py`)
- Random Forest regression model
- 5-year salary predictions (2025-2030)
- Confidence interval calculations
- Feature engineering
- Model validation and metrics

#### 3. Visualization Generator (`visualizations.py`)
- Creates Plotly charts (bar, line, scatter)
- Exports charts as JSON for frontend
- Handles color schemes and branding
- Responsive chart configurations

#### 4. Utilities (`utils.py`)
- Currency formatting
- Date/time handling
- Color palette management
- Helper functions

### Frontend Components

#### 1. Main Application (`App.tsx`)
- Top-level component
- Route management
- Global state
- API integration

#### 2. Dashboard Views
- Overview Dashboard
- Salary Explorer
- Forecast Dashboard
- Economic Context
- Legal Context

#### 3. Sidebar Filters
- Multi-select checkboxes
- Filter state management
- Real-time updates

## API Design

### RESTful Endpoints

```
Base URL: http://localhost:5000/api

Data Management:
  POST   /init               Initialize with dataset
  POST   /upload             Upload custom CSV/XLSX
  GET    /status             Check data load status

Data Retrieval:
  GET    /data/summary       Dataset statistics
  GET    /data/salaries      All salary records
  GET    /data/by-country    Country aggregations
  GET    /data/by-role       Role aggregations
  GET    /economic           Economic indicators
  GET    /legal              Legal/cultural data

Analysis:
  GET    /forecast           5-year salary forecast
                             ?country=Germany&role=DevOps Engineer
```

## Data Flow

### 1. Data Loading Flow
```
User Request → Backend API → Data Processor → 
Load Excel → Validate → Clean → Store in Memory → Return Status
```

### 2. Query Flow
```
User Filter Selection → Frontend State Update → 
API Request with Filters → Backend Processing → 
Filter Data → Aggregate → Return JSON → Frontend Render
```

### 3. Forecast Flow
```
User Selects Country/Role → API Request → 
Load Historical Data → Feature Engineering → 
Train Random Forest → Generate Predictions → 
Calculate Confidence Intervals → Return Forecast
```

## Deployment Architecture

### Development
- Frontend: Vite dev server (port 5173)
- Backend: Flask dev server (port 5000)
- Hot module reloading enabled

### Production
- Frontend: Built static files served via nginx/Apache
- Backend: Gunicorn WSGI server with multiple workers
- Reverse proxy for SSL termination
- Optional: Docker containers with docker-compose

### Docker Deployment
```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   Nginx     │──────▶│   Frontend  │       │   Backend   │
│  (Port 80)  │       │  Container  │◀─────▶│  Container  │
└─────────────┘       └─────────────┘       └─────────────┘
                      Static Files          Flask + Gunicorn
```

## Security Considerations

### CORS Configuration
- Configured for localhost development
- Restrictive origins in production
- Credentials support disabled

### Data Validation
- Input sanitization on uploads
- File type restrictions (CSV, XLSX only)
- Size limits (16MB max)
- SQL injection prevention (no direct SQL)

### Best Practices
- Environment variables for secrets
- HTTPS in production
- Rate limiting recommended
- Error messages sanitized

## Performance Optimization

### Backend
- In-memory data caching
- Efficient pandas operations
- Vectorized computations
- Lazy loading where possible

### Frontend
- Code splitting with Vite
- Component memoization
- Debounced filter updates
- Virtual scrolling for large tables

## Scalability Considerations

### Current Architecture
- Single-server deployment
- In-memory data storage
- Synchronous processing

### Future Enhancements
- PostgreSQL/MySQL for persistence
- Redis for caching
- Celery for async tasks
- Load balancing for horizontal scaling
- CDN for static assets

## Monitoring & Logging

### Backend Logging
- Flask request/response logging
- Error tracking
- Performance metrics
- User activity logs

### Frontend Monitoring
- Console error tracking
- API request monitoring
- User interaction analytics
- Performance timing

## Development Workflow

### Local Development
1. Clone repository
2. Install dependencies (backend + frontend)
3. Start backend server (port 5000)
4. Start frontend dev server (port 5173)
5. Access at http://localhost:5173

### Testing Strategy
- Unit tests for backend functions
- Integration tests for API endpoints
- Component tests for React components
- End-to-end tests for critical flows

## Documentation Standards

- Code comments for complex logic
- Docstrings for Python functions
- JSDoc for TypeScript functions
- README for setup instructions
- API documentation with examples

---

**Last Updated**: January 2025  
**Version**: 1.0.0  
**Maintained by**: BMW x ISM Field Project Team
