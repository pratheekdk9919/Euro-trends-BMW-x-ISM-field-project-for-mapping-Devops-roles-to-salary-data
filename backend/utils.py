import pandas as pd
import numpy as np
from typing import List
from datetime import datetime

def format_currency(amount, currency: str = "Euro") -> str:
    """Format amount as currency in Euro."""
    if pd.isna(amount) or amount == 0:
        return "€0"
    
    # Handle string input that might come from hover templates
    if isinstance(amount, str):
        try:
            amount = float(amount.replace('€', '').replace(',', ''))
        except:
            return "€0"
    
    # Convert to float if needed
    try:
        amount = float(amount)
    except:
        return "€0"
    
    # Format with thousands separator
    if amount >= 1000000:
        return f"€{amount/1000000:.1f}M"
    elif amount >= 1000:
        return f"€{amount/1000:.0f}K"
    else:
        return f"€{amount:.0f}"

def get_vibrant_colors() -> List[str]:
    """Return a list of vibrant colors for charts."""
    return [
        '#FF6B6B',  # Red
        '#4ECDC4',  # Teal
        '#45B7D1',  # Blue
        '#96CEB4',  # Green
        '#FFEAA7',  # Yellow
        '#DDA0DD',  # Plum
        '#98D8C8',  # Mint
        '#F7DC6F',  # Gold
        '#BB8FCE',  # Purple
        '#85C1E9',  # Sky Blue
        '#F8C471',  # Orange
        '#82E0AA',  # Light Green
        '#F1948A',  # Pink
        '#85CDFD',  # Bright Blue
        '#FFB74D',  # Amber
        '#CE93D8'   # Lavender
    ]

def get_bmw_colors() -> List[str]:
    """Return BMW-inspired color palette."""
    return [
        '#003087',  # BMW Blue
        '#666666',  # Gray
        '#FFFFFF',  # White
        '#1976D2',  # Light Blue
        '#424242',  # Dark Gray
        '#E3F2FD',  # Very Light Blue
        '#90CAF9',  # Lighter Blue
        '#2196F3'   # Medium Blue
    ]

def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """Calculate percentage change between two values."""
    if old_value == 0:
        return 0.0
    return ((new_value - old_value) / old_value) * 100

def validate_data_structure(data: pd.DataFrame, required_columns: List[str]) -> dict:
    """Validate if DataFrame has required columns."""
    missing_columns = [col for col in required_columns if col not in data.columns]
    extra_columns = [col for col in data.columns if col not in required_columns]
    
    return {
        'is_valid': len(missing_columns) == 0,
        'missing_columns': missing_columns,
        'extra_columns': extra_columns,
        'total_rows': len(data)
    }

def clean_numeric_column(series: pd.Series) -> pd.Series:
    """Clean and convert series to numeric, handling various formats."""
    # Remove common currency symbols and separators
    if series.dtype == 'object':
        series = series.str.replace('€', '').str.replace('$', '')
        series = series.str.replace(',', '').str.strip()
    
    return pd.to_numeric(series, errors='coerce')

def generate_country_flag_emoji(country: str) -> str:
    """Generate flag emoji for country (fallback to text)."""
    flag_map = {
        'Germany': '🇩🇪',
        'Hungary': '🇭🇺',
        'Poland': '🇵🇱',
        'India': '🇮🇳'
    }
    return flag_map.get(country, '🏁')

def create_summary_stats(data: pd.DataFrame, column: str) -> dict:
    """Create summary statistics for a numeric column."""
    if column not in data.columns:
        return {}
    
    series = data[column].dropna()
    
    if len(series) == 0:
        return {}
    
    return {
        'count': len(series),
        'mean': series.mean(),
        'median': series.median(),
        'std': series.std(),
        'min': series.min(),
        'max': series.max(),
        'q25': series.quantile(0.25),
        'q75': series.quantile(0.75)
    }

def format_large_number(number: float) -> str:
    """Format large numbers with appropriate suffixes."""
    if abs(number) >= 1e9:
        return f"{number/1e9:.1f}B"
    elif abs(number) >= 1e6:
        return f"{number/1e6:.1f}M"
    elif abs(number) >= 1e3:
        return f"{number/1e3:.1f}K"
    else:
        return f"{number:.0f}"

def get_trend_direction(values: List[float]) -> str:
    """Determine trend direction from a list of values."""
    if len(values) < 2:
        return "Insufficient data"
    
    # Calculate overall trend using linear regression
    x = np.arange(len(values))
    y = np.array(values)
    
    # Remove NaN values
    mask = ~np.isnan(y)
    if mask.sum() < 2:
        return "Insufficient data"
    
    x_clean = x[mask]
    y_clean = y[mask]
    
    # Calculate slope
    coefficients = np.polyfit(x_clean, y_clean, 1)
    slope = coefficients[0]
    
    if slope > 0.01:
        return "↗ Upward"
    elif slope < -0.01:
        return "↘ Downward"
    else:
        return "→ Stable"

def create_export_filename(base_name: str, extension: str = "csv") -> str:
    """Create a timestamped export filename."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.{extension}"
