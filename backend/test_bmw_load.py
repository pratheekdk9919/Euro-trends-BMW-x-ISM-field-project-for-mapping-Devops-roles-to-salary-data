import pandas as pd
import os

path = os.path.join(os.path.dirname(__file__), '..', 'BMW Data Set for WebApp.xlsx')
print(f"Loading: {path}")
print(f"Exists: {os.path.exists(path)}")

try:
    df = pd.read_excel(path)
    print(f"✓ Loaded {len(df)} rows")
    print(f"\nColumn names:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. '{col}'")
    
    # Process the data
    processed_df = pd.DataFrame({
        'Country': df['country'].fillna('Unknown'),
        'Role': df['job_role'].fillna('Unknown'),
        'Experience_Level': df['level_of_experience'].fillna('Unknown'),
        'Years_of_Experience': df['years_of_experience'].fillna(0),
        'Salary_EUR': df['salary adjusted to euro'].fillna(0),
        'Skills': df['skills'].fillna(''),
        'Location': df['location'].fillna('Unknown'),
        'Salary_Range': df['salary_range'].fillna('')
    })
    
    # Filter out rows with zero salary
    processed_df = processed_df[processed_df['Salary_EUR'] > 0]
    
    print(f"✓ Processed {len(processed_df)} valid records")
    print(f"\nSample data:")
    print(processed_df.head(3))
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
