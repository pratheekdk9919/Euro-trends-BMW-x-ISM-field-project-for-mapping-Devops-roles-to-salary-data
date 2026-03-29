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
    print("[OK] data_processor imported successfully")
except Exception as e:
    print(f"[FAIL] data_processor import failed: {e}")
    sys.exit(1)

try:
    from forecasting import SalaryForecaster
    print("[OK] forecasting imported successfully")
except Exception as e:
    print(f"[FAIL] forecasting import failed: {e}")
    sys.exit(1)

try:
    from visualizations import ChartGenerator
    print("[OK] visualizations imported successfully")
except Exception as e:
    print(f"[FAIL] visualizations import failed: {e}")
    sys.exit(1)

try:
    from utils import format_currency
    print("[OK] utils imported successfully")
except Exception as e:
    print(f"[FAIL] utils import failed: {e}")
    sys.exit(1)

# Test 2: Data Processor
print("\n[2] Testing DataProcessor...")
try:
    dp = DataProcessor()
    demo_data = dp._create_default_data()
    print(f"[OK] Demo data created: {len(demo_data['salary_data'])} salary records")
    print(f"[OK] Countries: {demo_data['salary_data']['Country'].unique().tolist()}")
except Exception as e:
    print(f"[FAIL] DataProcessor test failed: {e}")
    import traceback
    traceback.print_exc()

# Test 3: Forecasting
print("\n[3] Testing SalaryForecaster...")
try:
    forecaster = SalaryForecaster()
    forecast = forecaster.generate_forecast(demo_data['salary_data'])
    print(f"[OK] Forecast generated: {len(forecast)} records")
except Exception as e:
    print(f"[FAIL] Forecasting test failed: {e}")
    import traceback
    traceback.print_exc()

# Test 4: Visualizations
print("\n[4] Testing ChartGenerator...")
try:
    chart_gen = ChartGenerator()
    chart = chart_gen.create_country_salary_chart(demo_data['salary_data'])
    print(f"[OK] Chart created successfully")
except Exception as e:
    print(f"[FAIL] Chart generation failed: {e}")
    import traceback
    traceback.print_exc()

# Test 5: Flask app import
print("\n[5] Testing Flask app import...")
try:
    from flask import Flask
    print("[OK] Flask imported successfully")
    
    # Try to import the app
    import app as flask_app
    print(f"[OK] Flask app module imported")
    print(f"[OK] Flask app object: {flask_app.app}")
except Exception as e:
    print(f"[FAIL] Flask app import failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("ALL TESTS COMPLETED")
print("="*60)
