# BMW DevOps Salary Dashboard

## Overview

This is a Streamlit-based web application for BMW's DevOps salary mapping and forecasting project. The application provides comprehensive salary analysis across multiple countries (Germany, Hungary, Poland, India) with forecasting capabilities and interactive visualizations. It's designed to help BMW make informed decisions about DevOps team salaries and resource allocation.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit (Python-based web framework)
- **UI Components**: Streamlit widgets for file upload, filters, and interactive elements
- **Layout**: Wide layout with expandable sidebar for controls
- **State Management**: Streamlit session state for maintaining application state across interactions

### Backend Architecture
- **Language**: Python
- **Architecture Pattern**: Modular design with separate classes for different concerns
- **Data Processing**: Pandas for data manipulation and analysis
- **Machine Learning**: Scikit-learn for salary forecasting models
- **Visualization**: Plotly for interactive charts and graphs

## Key Components

### 1. Data Processing (`data_processor.py`)
- **Purpose**: Handles data ingestion, validation, and preprocessing
- **Key Features**:
  - Multi-format file support (Excel, CSV)
  - Data validation against required schema
  - Automatic data type detection and extraction
  - Default data generation for demo purposes
- **Required Data Schemas**:
  - Salary data: Role_Name, Country, Team_Setup, Salary_Min/Max/Avg_USD
  - Economic data: Country, Inflation_Rate, PPP_Adjustment, GDP_Growth, Cost_of_Living_Index
  - Legal data: Country, Labor_Laws, Tax_Implications, Workforce_Sentiment

### 2. Forecasting Engine (`forecasting.py`)
- **Purpose**: Generates 5-year salary forecasts using machine learning
- **Key Features**:
  - Linear and polynomial regression models
  - Country-specific economic growth factors
  - Role-based salary projections
  - Inflation and market demand adjustments
- **Forecast Period**: 2025-2030
- **Methodology**: Combines historical data with economic indicators

### 3. Visualization Generator (`visualizations.py`)
- **Purpose**: Creates interactive charts and graphs
- **Key Features**:
  - Country-wise salary comparisons
  - Role-based salary analysis
  - BMW-themed color schemes
  - Responsive chart layouts
- **Chart Types**: Bar charts, line graphs, comparison charts

### 4. Main Application (`app.py`)
- **Purpose**: Orchestrates the entire application
- **Key Features**:
  - File upload interface
  - Data filtering and selection
  /* Lines omitted */
  - Session state management

### 5. Utilities (`utils.py`)
- **Purpose**: Provides common utility functions
- **Key Features**:
  - Currency formatting (Ruro currency)
  /* Lines omitted */
  - BMW brand-specific styling

## Data Flow

1. **Data Input**: Users upload Excel/CSV files containing salary data
2. **Data Validation**: DataProcessor validates and structures the data
3. **Data Processing**: Raw data is cleaned and organized into structured formats
4. **Forecasting**: SalaryForecaster generates predictions based on economic factors
5. **Visualization**: ChartGenerator creates interactive charts
6. **Display**: Results are rendered in the Streamlit interface

## External Dependencies

### Core Libraries
- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **plotly**: Interactive visualization library
- **scikit-learn**: Machine learning algorithms

### Data Sources
- File uploads (Excel/CSV format)
- Economic indicators (inflation, GDP, cost of living)
- Legal and cultural factors by country

### Supported File Formats
- Excel (.xlsx)
- CSV (.csv)

## Deployment Strategy

### Current Setup
- **Platform**: Streamlit application (can be deployed on Streamlit Cloud, Heroku, or similar)
- **Dependencies**: Requirements managed via Python package manager
- **Configuration**: Page configuration set for wide layout and BMW branding

### Deployment Options
1. **Streamlit Cloud**: Direct deployment from GitHub repository
2. **Heroku**: Container-based deployment
3. **Local Development**: Run using `streamlit run app.py`

### Configuration Requirements
- Python 3.7+
- All dependencies listed in requirements.txt
- Sufficient memory for data processing and visualization

## Changelog

- June 27, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.
