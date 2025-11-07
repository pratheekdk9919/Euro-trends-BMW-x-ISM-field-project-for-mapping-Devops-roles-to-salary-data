import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils import format_currency, get_vibrant_colors

class ChartGenerator:
    def __init__(self):
        self.colors = get_vibrant_colors()
        self.bmw_blue = '#003087'
        self.layout_config = {
            'font': {'family': 'Arial, sans-serif'},
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
        }
    
    def create_country_salary_chart(self, data: pd.DataFrame) -> go.Figure:
        """Create vibrant bar chart showing average salaries by country."""
        country_data = data.groupby('Country')['Salary_Avg_USD'].mean().reset_index()
        country_data['Salary_Formatted'] = country_data['Salary_Avg_USD'].apply(format_currency)
        
        fig = px.bar(
            country_data,
            x='Country',
            y='Salary_Avg_USD',
            title='Average DevOps Salaries by Country',
            color='Country',
            color_discrete_sequence=self.colors,
            text='Salary_Formatted'
        )
        
        fig.update_traces(textposition='outside')
        fig.update_layout(
            **self.layout_config,
            xaxis_title='Country',
            yaxis_title='Average Salary (Euro)',
            showlegend=False,
            title_font_size=16,
            title_font_color=self.bmw_blue
        )
        
        return fig
    
    def create_role_salary_chart(self, data: pd.DataFrame) -> go.Figure:
        """Create vibrant bar chart showing average salaries by role."""
        role_data = data.groupby('Role_Name')['Salary_Avg_USD'].mean().reset_index()
        role_data = role_data.sort_values('Salary_Avg_USD', ascending=True)
        role_data['Salary_Formatted'] = role_data['Salary_Avg_USD'].apply(format_currency)
        
        fig = px.bar(
            role_data,
            x='Salary_Avg_USD',
            y='Role_Name',
            title='Average Salaries by DevOps Role',
            color='Salary_Avg_USD',
            color_continuous_scale='Viridis',
            text='Salary_Formatted',
            orientation='h'
        )
        
        fig.update_traces(textposition='outside')
        fig.update_layout(
            **self.layout_config,
            xaxis_title='Average Salary (Euro)',
            yaxis_title='Role',
            title_font_size=16,
            title_font_color=self.bmw_blue,
            coloraxis_showscale=False
        )
        
        return fig
    
    def create_team_setup_chart(self, data: pd.DataFrame) -> go.Figure:
        """Create vibrant sunburst chart showing team setup distribution."""
        team_data = data.groupby(['Team_Setup', 'Country']).size().reset_index(name='Count')
        
        fig = px.sunburst(
            team_data,
            path=['Team_Setup', 'Country'],
            values='Count',
            title='DevOps Team Setup Distribution',
            color='Count',
            color_continuous_scale='Rainbow'
        )
        
        fig.update_layout(
            **self.layout_config,
            title_font_size=16,
            title_font_color=self.bmw_blue
        )
        
        return fig
    
    def create_salary_heatmap(self, data: pd.DataFrame) -> go.Figure:
        """Create vibrant heatmap showing salary distribution across countries and roles."""
        # Create pivot table
        heatmap_data = data.pivot_table(
            values='Salary_Avg_USD',
            index='Role_Name',
            columns='Country',
            aggfunc='mean'
        )
        
        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale='Plasma',
            text=[[format_currency(val) if not pd.isna(val) else 'N/A' 
                   for val in row] for row in heatmap_data.values],
            texttemplate="%{text}",
            textfont={"size": 10},
            hoverongaps=False
        ))
        
        fig.update_layout(
            **self.layout_config,
            title='Salary Heatmap: Roles vs Countries',
            xaxis_title='Country',
            yaxis_title='Role',
            title_font_size=16,
            title_font_color=self.bmw_blue
        )
        
        return fig
    
    def create_forecast_chart(self, forecast_data: pd.DataFrame, group_by: str) -> go.Figure:
        """Create line chart showing salary forecasts."""
        if forecast_data.empty:
            return go.Figure()
        
        year_cols = [col for col in forecast_data.columns if col.startswith('Year_')]
        
        fig = go.Figure()
        
        if group_by == 'Country':
            for country in forecast_data['Country'].unique():
                country_data = forecast_data[forecast_data['Country'] == country]
                y_values = country_data[year_cols].mean().values
                x_values = [int(col.split('_')[1]) for col in year_cols]
                
                fig.add_trace(go.Scatter(
                    x=x_values,
                    y=y_values,
                    mode='lines+markers',
                    name=country,
                    line=dict(width=3),
                    marker=dict(size=8)
                ))
        else:  # group_by == 'Role'
            for role in forecast_data['Role_Name'].unique():
                role_data = forecast_data[forecast_data['Role_Name'] == role]
                y_values = role_data[year_cols].mean().values
                x_values = [int(col.split('_')[1]) for col in year_cols]
                
                fig.add_trace(go.Scatter(
                    x=x_values,
                    y=y_values,
                    mode='lines+markers',
                    name=role,
                    line=dict(width=3),
                    marker=dict(size=8)
                ))
        
        fig.update_layout(
            **self.layout_config,
            title=f'5-Year Salary Forecast by {group_by}',
            xaxis_title='Year',
            yaxis_title='Average Salary (Euro)',
            title_font_size=16,
            title_font_color=self.bmw_blue,
            legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02)
        )
        
        return fig
    
    def create_economic_chart(self, data: pd.DataFrame, metric: str, title: str) -> go.Figure:
        """Create bar chart for economic metrics."""
        if data.empty or metric not in data.columns:
            return go.Figure()
        
        fig = px.bar(
            data,
            x='Country',
            y=metric,
            title=title,
            color='Country',
            color_discrete_sequence=self.colors,
            text=metric
        )
        
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(
            **self.layout_config,
            xaxis_title='Country',
            yaxis_title=metric.replace('_', ' '),
            showlegend=False,
            title_font_size=16,
            title_font_color=self.bmw_blue
        )
        
        return fig
    
    def create_sentiment_chart(self, data: pd.DataFrame) -> go.Figure:
        """Create pie chart for workforce sentiment distribution."""
        if data.empty or 'Workforce_Sentiment' not in data.columns:
            return go.Figure()
        
        sentiment_counts = data['Workforce_Sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']
        
        fig = px.pie(
            sentiment_counts,
            values='Count',
            names='Sentiment',
            title='Workforce Sentiment Distribution',
            color_discrete_sequence=self.colors
        )
        
        fig.update_layout(
            **self.layout_config,
            title_font_size=16,
            title_font_color=self.bmw_blue
        )
        
        return fig
    
    def create_comparison_chart(self, data: pd.DataFrame) -> go.Figure:
        """Create comparison chart for salary ranges."""
        if data.empty:
            return go.Figure()
        
        fig = go.Figure()
        
        for country in data['Country'].unique():
            country_data = data[data['Country'] == country]
            
            fig.add_trace(go.Box(
                y=country_data['Salary_Avg_USD'],
                name=country,
                marker_color=self.colors[list(data['Country'].unique()).index(country) % len(self.colors)]
            ))
        
        fig.update_layout(
            **self.layout_config,
            title='Salary Distribution by Country',
            yaxis_title='Salary (Euro)',
            title_font_size=16,
            title_font_color=self.bmw_blue
        )
        
        return fig
