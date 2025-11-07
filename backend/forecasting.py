import pandas as pd
import numpy as np
import warnings
from typing import Dict, Any
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

warnings.filterwarnings('ignore')

class SalaryForecaster:
    def __init__(self):
        self.forecast_years = [2025, 2026, 2027, 2028, 2029, 2030]
        self.base_year = 2025
    
    def generate_forecast(self, salary_data: pd.DataFrame) -> pd.DataFrame:
        """Generate 5-year salary forecasts for all roles and countries."""
        forecasts = []
        
        # Group by country and role for individual forecasts
        groups = salary_data.groupby(['Country', 'Role_Name'])
        
        for (country, role), group in groups:
            avg_salary = group['Salary_Avg_USD'].mean()
            growth_factors = self._get_growth_factors(country)
            forecast = self._forecast_role_salary(avg_salary, country, role, growth_factors)
            forecasts.append(forecast)
        
        if not forecasts:
            return pd.DataFrame()
        
        forecast_df = pd.DataFrame(forecasts)
        return forecast_df
    
    def _get_growth_factors(self, country: str) -> Dict[str, float]:
        """Get growth factors based on country economic conditions."""
        country_factors = {
            'Germany': {
                'inflation': 0.031,
                'demand_growth': 0.025,
                'market_maturity': 0.015,
                'tech_adoption': 0.02
            },
            'Hungary': {
                'inflation': 0.040,
                'demand_growth': 0.035,
                'market_maturity': 0.025,
                'tech_adoption': 0.03
            },
            'Poland': {
                'inflation': 0.032,
                'demand_growth': 0.030,
                'market_maturity': 0.028,
                'tech_adoption': 0.025
            },
            'India': {
                'inflation': 0.055,
                'demand_growth': 0.065,
                'market_maturity': 0.045,
                'tech_adoption': 0.055
            }
        }
        
        return country_factors.get(country, {
            'inflation': 0.035,
            'demand_growth': 0.030,
            'market_maturity': 0.025,
            'tech_adoption': 0.030
        })
    
    def _forecast_role_salary(self, base_salary: float, country: str, role: str, 
                            growth_factors: Dict[str, float]) -> Dict[str, Any]:
        """Forecast salary for a specific role and country."""
        # Calculate compound growth rate
        annual_growth = (
            growth_factors['inflation'] + 
            growth_factors['demand_growth'] + 
            growth_factors['market_maturity'] + 
            growth_factors['tech_adoption']
        )
        
        # Add role-specific growth adjustments
        role_multiplier = self._get_role_growth_multiplier(role)
        annual_growth *= role_multiplier
        
        # Add some controlled randomness for realism
        np.random.seed(hash(country + role) % 1000)
        volatility = np.random.normal(1.0, 0.02, len(self.forecast_years))
        
        forecast_data = {
            'Country': country,
            'Role_Name': role,
            'Base_Salary': base_salary
        }
        
        # Generate yearly forecasts
        for i, year in enumerate(self.forecast_years):
            years_ahead = i
            projected_salary = base_salary * ((1 + annual_growth) ** years_ahead) * volatility[i]
            forecast_data[f'Year_{year}'] = projected_salary
        
        return forecast_data
    
    def _get_role_growth_multiplier(self, role: str) -> float:
        """Get growth multiplier based on role demand trends."""
        role_multipliers = {
            'DevOps Engineer': 1.0,
            'Site Reliability Engineer': 1.15,
            'Platform Engineer': 1.20,
            'Cloud Engineer': 1.10,
            'Infrastructure Engineer': 0.95,
            'DevSecOps Engineer': 1.25,
            'Automation Engineer': 1.05,
            'Release Engineer': 0.90,
            'Systems Engineer': 0.85
        }
        return role_multipliers.get(role, 1.0)
    
    def calculate_growth_rates(self, forecast_data: pd.DataFrame) -> Dict[str, Any]:
        """Calculate various growth rate metrics from forecast data."""
        if forecast_data.empty:
            return {
                'overall_growth': 0,
                'min_growth': 0,
                'max_growth': 0,
                'avg_annual_growth': 0
            }
        
        # Calculate overall average growth rate
        start_col = 'Year_2025'
        end_col = 'Year_2030'
        
        if start_col in forecast_data.columns and end_col in forecast_data.columns:
            start_avg = forecast_data[start_col].mean()
            end_avg = forecast_data[end_col].mean()
            overall_growth = ((end_avg - start_avg) / start_avg) * 100
            avg_annual_growth = overall_growth / 5
        else:
            overall_growth = 0
            avg_annual_growth = 0
        
        return {
            'overall_growth': overall_growth,
            'avg_annual_growth': avg_annual_growth,
            'min_growth': forecast_data[end_col].min() if end_col in forecast_data.columns else 0,
            'max_growth': forecast_data[end_col].max() if end_col in forecast_data.columns else 0
        }
    
    def get_forecast_summary(self, forecast_data: pd.DataFrame) -> pd.DataFrame:
        """Get a summary of forecast data."""
        if forecast_data.empty:
            return pd.DataFrame()
        
        summary_data = []
        for _, row in forecast_data.iterrows():
            summary_data.append({
                'Country': row['Country'],
                'Role': row['Role_Name'],
                'Current (2025)': row.get('Year_2025', 0),
                'Projected (2030)': row.get('Year_2030', 0),
                'Growth': ((row.get('Year_2030', 0) - row.get('Year_2025', 0)) / row.get('Year_2025', 1)) * 100
            })
        
        return pd.DataFrame(summary_data)
