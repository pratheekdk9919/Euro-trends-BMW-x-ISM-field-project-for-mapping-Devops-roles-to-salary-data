import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

from data_processor import DataProcessor
from forecasting import SalaryForecaster
from visualizations import ChartGenerator
from utils import format_currency, get_vibrant_colors

# Page configuration
st.set_page_config(
    page_title="BMW DevOps Salary Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'data_processor' not in st.session_state:
    st.session_state.data_processor = DataProcessor()
if 'forecaster' not in st.session_state:
    st.session_state.forecaster = SalaryForecaster()
if 'chart_generator' not in st.session_state:
    st.session_state.chart_generator = ChartGenerator()

def main():
    st.title("BMW DevOps Salary Dashboard")
    st.markdown("---")
    
    # Sidebar for file upload and filters
    with st.sidebar:
        st.header("Data Upload")
        
        uploaded_file = st.file_uploader("Upload salary data (CSV/Excel)", type=['csv', 'xlsx'])
        
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    raw_data = pd.read_csv(uploaded_file)
                else:
                    raw_data = pd.read_excel(uploaded_file)
                
                processed_data = st.session_state.data_processor.process_raw_data(raw_data)
                st.session_state.salary_data = processed_data['salary_data']
                st.session_state.economic_data = processed_data['economic_data']
                st.session_state.legal_data = processed_data['legal_data']
                
                st.success("Data uploaded successfully!")
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")
        
        st.markdown("---")
        st.header("Filters")
    
    # Main content area
    if 'salary_data' not in st.session_state:
        st.info("Please upload salary data or the dashboard will use demo data.")
        default_data = st.session_state.data_processor._create_default_data()
        st.session_state.salary_data = default_data['salary_data']
        st.session_state.economic_data = default_data['economic_data']
        st.session_state.legal_data = default_data['legal_data']
    
    # Filters in sidebar
    with st.sidebar:
        all_countries = st.session_state.salary_data['Country'].unique().tolist()
        countries = st.multiselect("Select Countries", all_countries, default=all_countries)
        
        all_roles = st.session_state.salary_data['Role_Name'].unique().tolist()
        roles = st.multiselect("Select Roles", all_roles, default=all_roles)
        
        all_team_setups = st.session_state.salary_data['Team_Setup'].unique().tolist()
        team_setups = st.multiselect("Select Team Setup", all_team_setups, default=all_team_setups)
    
    # Filter data based on selections
    filtered_data = st.session_state.salary_data[
        (st.session_state.salary_data['Country'].isin(countries)) &
        (st.session_state.salary_data['Role_Name'].isin(roles)) &
        (st.session_state.salary_data['Team_Setup'].isin(team_setups))
    ]
    
    if filtered_data.empty:
        st.warning("No data matches the selected filters. Please adjust your selections.")
        return
    
    # Dashboard tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Overview", 
        "Salary Explorer", 
        "5-Year Forecast", 
        "Economic Context", 
        "Legal & Cultural"
    ])
    
    with tab1:
        show_overview_dashboard(filtered_data)
    
    with tab2:
        show_salary_explorer(filtered_data)
    
    with tab3:
        show_forecast_dashboard(filtered_data)
    
    with tab4:
        show_economic_dashboard()
    
    with tab5:
        show_legal_cultural_dashboard()

def show_overview_dashboard(data):
    st.header("Salary Overview Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_salary = data['Salary_Avg_USD'].mean()
        st.metric(
            label="Average Salary",
            value=format_currency(avg_salary),
            delta=None
        )
    
    with col2:
        min_salary = data['Salary_Avg_USD'].min()
        st.metric(
            label="Min Salary",
            value=format_currency(min_salary)
        )
    
    with col3:
        max_salary = data['Salary_Avg_USD'].max()
        st.metric(
            label="Max Salary",
            value=format_currency(max_salary)
        )
    
    with col4:
        num_roles = data['Role_Name'].nunique()
        st.metric(
            label="Total Roles",
            value=num_roles
        )
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        country_chart = st.session_state.chart_generator.create_country_salary_chart(data)
        st.plotly_chart(country_chart, width='stretch')
    
    with col2:
        role_chart = st.session_state.chart_generator.create_role_salary_chart(data)
        st.plotly_chart(role_chart, width='stretch')
    
    # Team Setup Analysis
    team_chart = st.session_state.chart_generator.create_team_setup_chart(data)
    st.plotly_chart(team_chart, width='stretch')

def show_salary_explorer(data):
    st.header("Interactive Salary Explorer")
    
    # Salary comparison matrix
    col1, col2 = st.columns([2, 1])
    
    with col1:
        heatmap = st.session_state.chart_generator.create_salary_heatmap(data)
        st.plotly_chart(heatmap, width='stretch')
    
    with col2:
        st.subheader("Salary Statistics")
        st.write(f"**Mean:** {format_currency(data['Salary_Avg_USD'].mean())}")
        st.write(f"**Median:** {format_currency(data['Salary_Avg_USD'].median())}")
        st.write(f"**Std Dev:** {format_currency(data['Salary_Avg_USD'].std())}")
        st.write(f"**Range:** {format_currency(data['Salary_Avg_USD'].max() - data['Salary_Avg_USD'].min())}")
    
    # Detailed data table
    st.subheader("Detailed Salary Data")
    
    # Format the data for display
    display_data = data.copy()
    display_data['Salary_Min'] = display_data['Salary_Min_USD'].apply(format_currency)
    display_data['Salary_Max'] = display_data['Salary_Max_USD'].apply(format_currency)
    display_data['Salary_Avg'] = display_data['Salary_Avg_USD'].apply(format_currency)
    
    # Select columns for display
    display_columns = ['Role_Name', 'Country', 'Team_Setup', 'Salary_Min', 'Salary_Avg', 'Salary_Max']
    st.dataframe(
        display_data[display_columns],
        width='stretch',
        hide_index=True
    )

def show_forecast_dashboard(data):
    st.header("5-Year Salary Forecast")
    
    # Generate forecasts
    forecast_data = st.session_state.forecaster.generate_forecast(data)
    
    if forecast_data.empty:
        st.warning("Unable to generate forecast with current data.")
        return
    
    # Forecast visualization
    col1, col2 = st.columns(2)
    
    with col1:
        country_forecast = st.session_state.chart_generator.create_forecast_chart(
            forecast_data, 'Country')
        st.plotly_chart(country_forecast, width='stretch')
    
    with col2:
        role_forecast = st.session_state.chart_generator.create_forecast_chart(
            forecast_data, 'Role')
        st.plotly_chart(role_forecast, width='stretch')
    
    # Growth analysis
    st.subheader("Growth Analysis")
    
    growth_analysis = st.session_state.forecaster.calculate_growth_rates(forecast_data)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Overall Growth (2025-2030)",
            value=f"{growth_analysis['overall_growth']:.1f}%"
        )
    
    with col2:
        st.metric(
            label="Average Annual Growth",
            value=f"{growth_analysis['avg_annual_growth']:.1f}%"
        )
    
    with col3:
        st.metric(
            label="Projected 2030 Max",
            value=format_currency(growth_analysis['max_growth'])
        )

def show_economic_dashboard():
    st.header("Economic Context")
    
    if 'economic_data' not in st.session_state or st.session_state.economic_data.empty:
        st.warning("No economic data available.")
        return
    
    economic_data = st.session_state.economic_data
    
    # Economic metrics
    col1, col2 = st.columns(2)
    
    with col1:
        inflation_chart = st.session_state.chart_generator.create_economic_chart(
            economic_data, 'Inflation_Rate', 'Inflation Rate by Country')
        st.plotly_chart(inflation_chart, width='stretch')
    
    with col2:
        gdp_chart = st.session_state.chart_generator.create_economic_chart(
            economic_data, 'GDP_Growth', 'GDP Growth by Country')
        st.plotly_chart(gdp_chart, width='stretch')
    
    # Economic data table
    st.subheader("Economic Indicators")
    st.dataframe(economic_data, width='stretch', hide_index=True)

def show_legal_cultural_dashboard():
    st.header("Legal & Cultural Context")
    
    if 'legal_data' not in st.session_state or st.session_state.legal_data.empty:
        st.warning("No legal/cultural data available.")
        return
    
    legal_data = st.session_state.legal_data
    
    # Sentiment chart
    sentiment_chart = st.session_state.chart_generator.create_sentiment_chart(legal_data)
    st.plotly_chart(sentiment_chart, width='stretch')
    
    # Legal data table
    st.subheader("Legal & Cultural Information")
    st.dataframe(legal_data, width='stretch', hide_index=True)

if __name__ == "__main__":
    main()
