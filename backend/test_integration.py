#!/usr/bin/env python
"""Simple test script to verify backend functionality"""

import sys
import os

print("="*60)
print("BACKEND INTEGRATION TEST")
print("="*60)

# Test 1: Imports
print("\n[1] Testing imports...")
try:
    from data_processor import DataProcessor
    print("✓ data_processor imported successfully")
except Exception as e:
    print(f"✗ data_processor import failed: {e}")
    sys.exit(1)

try:
    from forecasting import SalaryForecaster
    print("✓ forecasting imported successfully")
except Exception as e:
    print(f"✗ forecasting import failed: {e}")
    sys.exit(1)

try:
    from visualizations import ChartGenerator
    print("✓ visualizations imported successfully")
except Exception as e:
    print(f"✗ visualizations import failed: {e}")
    sys.exit(1)

try:
    from utils import format_currency
    print("✓ utils imported successfully")
except Exception as e:
    print(f"✗ utils import failed: {e}")
    sys.exit(1)

# Test 2: Data Processor
print("\n[2] Testing DataProcessor...")
try:
    dp = DataProcessor()
    demo_data = dp._create_default_data()
    print(f"✓ Demo data created: {len(demo_data['salary_data'])} salary records")
    print(f"✓ Countries: {demo_data['salary_data']['Country'].unique().tolist()}")
except Exception as e:
    print(f"✗ DataProcessor test failed: {e}")
    import traceback
    traceback.print_exc()

# Test 3: Forecasting
print("\n[3] Testing SalaryForecaster...")
try:
    forecaster = SalaryForecaster()
    forecast = forecaster.generate_forecast(demo_data['salary_data'])
    print(f"✓ Forecast generated: {len(forecast)} records")
except Exception as e:
    print(f"✗ Forecasting test failed: {e}")
    import traceback
    traceback.print_exc()

# Test 4: Visualizations
print("\n[4] Testing ChartGenerator...")
try:
    chart_gen = ChartGenerator()
    chart = chart_gen.create_country_salary_chart(demo_data['salary_data'])
    print(f"✓ Chart created successfully")
except Exception as e:
    print(f"✗ Chart generation failed: {e}")
    import traceback
    traceback.print_exc()

# Test 5: Flask app import
print("\n[5] Testing Flask app import...")
try:
    from flask import Flask
    print("✓ Flask imported successfully")
    
    # Try to import the app
    import app as flask_app
    print(f"✓ Flask app module imported")
    print(f"✓ Flask app object: {flask_app.app}")
except Exception as e:
    print(f"✗ Flask app import failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("ALL TESTS COMPLETED")
print("="*60)
