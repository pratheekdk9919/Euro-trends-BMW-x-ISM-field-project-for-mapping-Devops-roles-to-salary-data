import pandas as pd
import sys
import os

# Change to backend directory
os.chdir(os.path.dirname(__file__))

try:
    # Load BMW dataset
    df = pd.read_excel('../BMW Data Set for WebApp.xlsx')
    
    print("="*60)
    print("BMW DATASET ANALYSIS")
    print("="*60)
    
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    print("\nColumns:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")
    
    print("\nFirst 3 rows:")
    print(df.head(3).to_string())
    
    print("\n" + "="*60)
    print("Dataset loaded successfully!")
    print("="*60)
    
except Exception as e:
    print(f"Error loading dataset: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
