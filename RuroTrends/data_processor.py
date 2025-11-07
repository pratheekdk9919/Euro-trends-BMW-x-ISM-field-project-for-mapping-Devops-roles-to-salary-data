import pandas as pd
import numpy as np
from typing import Dict, Any

class DataProcessor:
    def __init__(self):
        self.required_salary_columns = [
            'Role_Name', 'Country', 'Team_Setup', 
            'Salary_Min_USD', 'Salary_Max_USD', 'Salary_Avg_USD'
        ]
        
        self.required_economic_columns = [
            'Country', 'Inflation_Rate', 'PPP_Adjustment', 
            'GDP_Growth', 'Cost_of_Living_Index'
        ]
        
        self.required_legal_columns = [
            'Country', 'Labor_Laws', 'Tax_Implications', 'Workforce_Sentiment'
        ]
    
    def process_raw_data(self, raw_data: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """Process raw uploaded data and extract different data types."""
        try:
            if self._is_combined_data(raw_data):
                return self._process_combined_data(raw_data)
            else:
                return self._process_salary_only_data(raw_data)
        except Exception as e:
            return self._create_default_data()
    
    def _is_combined_data(self, data: pd.DataFrame) -> bool:
        """Check if data contains multiple data types."""
        salary_cols = sum(1 for col in self.required_salary_columns if col in data.columns)
        economic_cols = sum(1 for col in self.required_economic_columns if col in data.columns)
        return salary_cols >= 4 and economic_cols >= 3
    
    def _process_combined_data(self, data: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """Process data that contains multiple data types."""
        salary_data = self._extract_salary_data(data)
        economic_data = self._extract_economic_data(data)
        legal_data = self._extract_legal_data(data)
        return {
            'salary_data': salary_data,
            'economic_data': economic_data,
            'legal_data': legal_data
        }
    
    def _process_salary_only_data(self, data: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """Process data that contains only salary information."""
        salary_data = self._extract_salary_data(data)
        countries = salary_data['Country'].unique().tolist()
        economic_data = self._create_default_economic_data(countries)
        legal_data = self._create_default_legal_data(countries)
        return {
            'salary_data': salary_data,
            'economic_data': economic_data,
            'legal_data': legal_data
        }
    
    def _extract_salary_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Extract and clean salary data."""
        if 'job_role' in data.columns and 'country' in data.columns:
            return self._process_bmw_dataset(data)
        
        column_mapping = self._map_columns(data, self.required_salary_columns)
        salary_data = data[list(column_mapping.keys())].copy()
        salary_data = salary_data.rename(columns=column_mapping)
        salary_data = self._clean_salary_data(salary_data)
        return salary_data
    
    def _process_bmw_dataset(self, data: pd.DataFrame) -> pd.DataFrame:
        """Process the specific BMW dataset format."""
        bmw_data = data.copy()
        salary_data = pd.DataFrame()
        
        salary_data['Role_Name'] = bmw_data['job_role']
        salary_data['Country'] = bmw_data['country']
        
        if 'team_setup' in bmw_data.columns:
            salary_data['Team_Setup'] = bmw_data['team_setup']
        else:
            salary_data['Team_Setup'] = bmw_data['job_role'].apply(self._categorize_team_setup)
        
        if 'salary_min' in bmw_data.columns:
            salary_data['Salary_Min_USD'] = bmw_data['salary_min']
        if 'salary_max' in bmw_data.columns:
            salary_data['Salary_Max_USD'] = bmw_data['salary_max']
        if 'salary_avg' in bmw_data.columns:
            salary_data['Salary_Avg_USD'] = bmw_data['salary_avg']
        elif 'Salary_Min_USD' in salary_data.columns and 'Salary_Max_USD' in salary_data.columns:
            salary_data['Salary_Avg_USD'] = (salary_data['Salary_Min_USD'] + salary_data['Salary_Max_USD']) / 2
        
        return self._clean_salary_data(salary_data)
    
    def _categorize_team_setup(self, role_name: str) -> str:
        """Categorize team setup based on role name."""
        role_lower = str(role_name).lower()
        if 'senior' in role_lower or 'lead' in role_lower:
            return 'On-site'
        elif 'junior' in role_lower:
            return 'Hybrid'
        else:
            return 'Remote'
    
    def _extract_economic_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Extract economic data from combined dataset."""
        column_mapping = self._map_columns(data, self.required_economic_columns)
        if not column_mapping:
            countries = data['Country'].unique() if 'Country' in data.columns else []
            return self._create_default_economic_data(countries)
        
        economic_data = data[list(column_mapping.keys())].copy()
        economic_data = economic_data.rename(columns=column_mapping)
        economic_data = economic_data.drop_duplicates(subset=['Country'])
        return economic_data
    
    def _extract_legal_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Extract legal/cultural data from combined dataset."""
        column_mapping = self._map_columns(data, self.required_legal_columns)
        if not column_mapping:
            countries = data['Country'].unique() if 'Country' in data.columns else []
            return self._create_default_legal_data(countries)
        
        legal_data = data[list(column_mapping.keys())].copy()
        legal_data = legal_data.rename(columns=column_mapping)
        legal_data = legal_data.drop_duplicates(subset=['Country'])
        return legal_data
    
    def _map_columns(self, data: pd.DataFrame, required_columns: list) -> Dict[str, str]:
        """Map actual column names to required column names."""
        column_mapping = {}
        for req_col in required_columns:
            for actual_col in data.columns:
                if self._is_similar_column(req_col, actual_col):
                    column_mapping[actual_col] = req_col
                    break
        return column_mapping
    
    def _is_similar_column(self, required: str, actual: str) -> bool:
        """Check if actual column name is similar to required column name."""
        req_lower = required.lower().replace('_', '').replace(' ', '')
        act_lower = actual.lower().replace('_', '').replace(' ', '')
        return req_lower == act_lower or req_lower in act_lower or act_lower in req_lower
    
    def _clean_salary_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Clean and validate salary data."""
        data = data.dropna(subset=['Role_Name', 'Country'])
        
        for col in ['Salary_Min_USD', 'Salary_Max_USD', 'Salary_Avg_USD']:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col], errors='coerce')
        
        if 'Salary_Avg_USD' not in data.columns or data['Salary_Avg_USD'].isna().all():
            if 'Salary_Min_USD' in data.columns and 'Salary_Max_USD' in data.columns:
                data['Salary_Avg_USD'] = (data['Salary_Min_USD'] + data['Salary_Max_USD']) / 2
        
        data = data.dropna(subset=['Salary_Avg_USD'])
        return data
    
    def _create_default_economic_data(self, countries: list) -> pd.DataFrame:
        """Create default economic data for countries."""
        default_economic = {
            'Germany': {'Inflation_Rate': 3.1, 'PPP_Adjustment': 1.0, 'GDP_Growth': 1.5, 'Cost_of_Living_Index': 110},
            'Hungary': {'Inflation_Rate': 4.0, 'PPP_Adjustment': 0.6, 'GDP_Growth': 2.5, 'Cost_of_Living_Index': 70},
            'Poland': {'Inflation_Rate': 3.2, 'PPP_Adjustment': 0.65, 'GDP_Growth': 3.0, 'Cost_of_Living_Index': 75},
            'India': {'Inflation_Rate': 5.5, 'PPP_Adjustment': 0.3, 'GDP_Growth': 6.5, 'Cost_of_Living_Index': 45}
        }
        
        economic_data = []
        for country in countries:
            if country in default_economic:
                row = {'Country': country}
                row.update(default_economic[country])
                economic_data.append(row)
        
        return pd.DataFrame(economic_data)
    
    def _create_default_legal_data(self, countries: list) -> pd.DataFrame:
        """Create default legal/cultural data for countries."""
        default_legal = {
            'Germany': {
                'Labor_Laws': 'Strong worker protection, comprehensive benefits',
                'Tax_Implications': 'Progressive tax system (14-45%), social security contributions',
                'Workforce_Sentiment': 'Positive'
            },
            'Hungary': {
                'Labor_Laws': 'EU-compliant labor regulations, flexible working arrangements',
                'Tax_Implications': 'Flat 15% personal income tax, social contributions',
                'Workforce_Sentiment': 'Neutral'
            },
            'Poland': {
                'Labor_Laws': 'EU standards, growing tech sector protections',
                'Tax_Implications': 'Progressive tax (17-32%), social contributions',
                'Workforce_Sentiment': 'Positive'
            },
            'India': {
                'Labor_Laws': 'Complex regulations, varying by state',
                'Tax_Implications': 'Progressive tax (5-30%), allowances and deductions',
                'Workforce_Sentiment': 'Very Positive'
            }
        }
        
        legal_data = []
        for country in countries:
            if country in default_legal:
                row = {'Country': country}
                row.update(default_legal[country])
                legal_data.append(row)
        
        return pd.DataFrame(legal_data)
    
    def _create_default_data(self) -> Dict[str, pd.DataFrame]:
        """Create complete default dataset for demonstration."""
        roles = ['DevOps Engineer', 'Site Reliability Engineer', 'Platform Engineer', 'Cloud Engineer']
        countries = ['Germany', 'Hungary', 'Poland', 'India']
        team_setups = ['On-site', 'Hybrid', 'Remote']
        
        salary_data = []
        for country in countries:
            for role in roles:
                for setup in team_setups:
                    base_salary = {
                        'Germany': 70000,
                        'Hungary': 45000,
                        'Poland': 50000,
                        'India': 25000
                    }[country]
                    
                    role_multiplier = {
                        'DevOps Engineer': 1.0,
                        'Site Reliability Engineer': 1.15,
                        'Platform Engineer': 1.20,
                        'Cloud Engineer': 1.10
                    }[role]
                    
                    avg_salary = base_salary * role_multiplier
                    
                    salary_data.append({
                        'Role_Name': role,
                        'Country': country,
                        'Team_Setup': setup,
                        'Salary_Min_USD': avg_salary * 0.85,
                        'Salary_Max_USD': avg_salary * 1.15,
                        'Salary_Avg_USD': avg_salary
                    })
        
        salary_df = pd.DataFrame(salary_data)
        economic_df = self._create_default_economic_data(countries)
        legal_df = self._create_default_legal_data(countries)
        
        return {
            'salary_data': salary_df,
            'economic_data': economic_df,
            'legal_data': legal_df
        }
