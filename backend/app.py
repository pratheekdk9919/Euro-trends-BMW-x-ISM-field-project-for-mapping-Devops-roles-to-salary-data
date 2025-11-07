from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import os
import pandas as pd
import json
from werkzeug.utils import secure_filename

# Import RuroTrends modules
from data_processor import DataProcessor
from forecasting import SalaryForecaster
from visualizations import ChartGenerator
from utils import format_currency, get_vibrant_colors

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize processors
data_processor = DataProcessor()
forecaster = SalaryForecaster()
chart_generator = ChartGenerator()

# In-memory data store (for demo purposes)
app_data = {
    'salary_data': None,
    'economic_data': None,
    'legal_data': None,
    'processed': False
}

# BMW Dataset path
BMW_DATASET_PATH = os.path.join(os.path.dirname(__file__), '..', 'BMW Data Set for WebApp.xlsx')

def load_bmw_dataset():
    """Load and process BMW dataset"""
    try:
        print(f"Loading BMW dataset from: {BMW_DATASET_PATH}")
        
        # Load the Excel file
        df = pd.read_excel(BMW_DATASET_PATH)
        
        print(f"Loaded {len(df)} records from BMW dataset")
        
        # Process and standardize the data to match expected format
        processed_df = pd.DataFrame({
            'Country': df['country'].fillna('Unknown'),
            'Role_Name': df['job_role'].fillna('Unknown'),  # Changed to Role_Name
            'Experience_Level': df['level_of_experience'].fillna('Unknown'),
            'Years_of_Experience': df['years_of_experience'].fillna(0),
            'Salary_EUR': df['salary adjusted to euro '].fillna(0),  # Note trailing space
            'Salary_Avg_USD': df['salary adjusted to euro '].fillna(0) * 1.1,  # Approximate USD conversion
            'Salary_Min_USD': df['salary adjusted to euro '].fillna(0) * 0.9,  # Approximate min
            'Salary_Max_USD': df['salary adjusted to euro '].fillna(0) * 1.3,  # Approximate max
            'Skills': df['skills'].fillna(''),
            'Location': df['location'].fillna('Unknown'),
            'Salary_Range': df['salary_range'].fillna(''),
            'Team_Setup': 'Hybrid'  # Default value as not in dataset
        })
        
        # Filter out rows with zero salary
        processed_df = processed_df[processed_df['Salary_EUR'] > 0]
        
        print(f"Processed {len(processed_df)} valid records")
        
        return processed_df
    except Exception as e:
        print(f"Error loading BMW dataset: {e}")
        import traceback
        traceback.print_exc()
        return None

def initialize_bmw_data():
    """Initialize app with BMW dataset"""
    global app_data
    
    bmw_data = load_bmw_dataset()
    
    if bmw_data is not None and len(bmw_data) > 0:
        app_data['salary_data'] = bmw_data
        app_data['economic_data'] = data_processor._create_default_data()['economic_data']
        app_data['legal_data'] = data_processor._create_default_data()['legal_data']
        app_data['processed'] = True
        print(f"✓ BMW dataset initialized with {len(bmw_data)} records")
        return True
    else:
        print("✗ Failed to load BMW dataset, using demo data instead")
        default_data = data_processor._create_default_data()
        app_data['salary_data'] = default_data['salary_data']
        app_data['economic_data'] = default_data['economic_data']
        app_data['legal_data'] = default_data['legal_data']
        app_data['processed'] = True
        return False

# Load BMW dataset on startup
print("\n" + "="*60)
print("INITIALIZING BACKEND WITH BMW DATASET")
print("="*60)
initialize_bmw_data()
print("="*60 + "\n")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/status')
def status():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok', 
        'service': 'euro-trends-backend',
        'version': '1.0.0',
        'data_loaded': app_data['processed']
    })

@app.route('/api/init', methods=['POST'])
def initialize_demo_data():
    """Initialize with BMW dataset (or demo data as fallback)"""
    try:
        success = initialize_bmw_data()
        
        return jsonify({
            'success': True,
            'message': 'BMW dataset loaded' if success else 'Demo data loaded (BMW dataset unavailable)',
            'records': len(app_data['salary_data']),
            'source': 'bmw_dataset' if success else 'demo_data'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload():
    """Upload and process dataset (CSV/Excel)"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Allowed: CSV, XLSX'}), 400
    
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the file
        if filename.endswith('.csv'):
            raw_data = pd.read_csv(filepath)
        else:
            raw_data = pd.read_excel(filepath)
        
        processed_data = data_processor.process_raw_data(raw_data)
        app_data['salary_data'] = processed_data['salary_data']
        app_data['economic_data'] = processed_data['economic_data']
        app_data['legal_data'] = processed_data['legal_data']
        app_data['processed'] = True
        
        return jsonify({
            'success': True,
            'filename': filename,
            'records': len(app_data['salary_data']),
            'countries': app_data['salary_data']['Country'].unique().tolist(),
            'roles': app_data['salary_data']['Role_Name'].unique().tolist()
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/data/summary', methods=['GET'])
def get_summary():
    """Get summary statistics of salary data"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded. Upload a file or initialize demo data.'}), 400
    
    try:
        salary_data = app_data['salary_data']
        
        summary = {
            'total_records': len(salary_data),
            'countries': salary_data['Country'].unique().tolist(),
            'roles': salary_data['Role_Name'].unique().tolist(),
            'team_setups': salary_data['Team_Setup'].unique().tolist(),
            'salary_stats': {
                'min': float(salary_data['Salary_Min_USD'].min()),
                'max': float(salary_data['Salary_Max_USD'].max()),
                'avg': float(salary_data['Salary_Avg_USD'].mean()),
                'median': float(salary_data['Salary_Avg_USD'].median()),
                'std': float(salary_data['Salary_Avg_USD'].std())
            }
        }
        
        return jsonify(summary)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data/salaries', methods=['GET'])
def get_salaries():
    """Get filtered salary data"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        salary_data = app_data['salary_data'].copy()
        
        # Apply filters from query parameters
        country = request.args.get('country')
        role = request.args.get('role')
        team_setup = request.args.get('team_setup')
        
        if country:
            salary_data = salary_data[salary_data['Country'] == country]
        if role:
            salary_data = salary_data[salary_data['Role_Name'] == role]
        if team_setup:
            salary_data = salary_data[salary_data['Team_Setup'] == team_setup]
        
        # Convert to JSON-friendly format
        result = salary_data.to_dict(orient='records')
        
        return jsonify({
            'success': True,
            'count': len(result),
            'data': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data/by-country', methods=['GET'])
def get_by_country():
    """Get salary data grouped by country"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        salary_data = app_data['salary_data']
        
        by_country = salary_data.groupby('Country').agg({
            'Salary_Avg_USD': ['mean', 'min', 'max', 'count']
        }).round(2)
        
        result = []
        for country in by_country.index:
            result.append({
                'country': country,
                'avg_salary': float(by_country.loc[country, ('Salary_Avg_USD', 'mean')]),
                'min_salary': float(by_country.loc[country, ('Salary_Avg_USD', 'min')]),
                'max_salary': float(by_country.loc[country, ('Salary_Avg_USD', 'max')]),
                'count': int(by_country.loc[country, ('Salary_Avg_USD', 'count')])
            })
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data/by-role', methods=['GET'])
def get_by_role():
    """Get salary data grouped by role"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        salary_data = app_data['salary_data']
        
        by_role = salary_data.groupby('Role_Name').agg({
            'Salary_Avg_USD': ['mean', 'min', 'max', 'count']
        }).round(2)
        
        result = []
        for role in by_role.index:
            result.append({
                'role': role,
                'avg_salary': float(by_role.loc[role, ('Salary_Avg_USD', 'mean')]),
                'min_salary': float(by_role.loc[role, ('Salary_Avg_USD', 'min')]),
                'max_salary': float(by_role.loc[role, ('Salary_Avg_USD', 'max')]),
                'count': int(by_role.loc[role, ('Salary_Avg_USD', 'count')])
            })
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    """Generate 5-year salary forecast"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        salary_data = app_data['salary_data']
        forecast_data = forecaster.generate_forecast(salary_data)
        
        if forecast_data.empty:
            return jsonify({'error': 'Unable to generate forecast'}), 400
        
        result = forecast_data.to_dict(orient='records')
        
        return jsonify({
            'success': True,
            'count': len(result),
            'data': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/charts/country-salary', methods=['GET'])
def get_country_salary_chart():
    """Get country salary comparison chart data"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        salary_data = app_data['salary_data']
        chart = chart_generator.create_country_salary_chart(salary_data)
        
        # Convert Plotly figure to JSON
        return jsonify(json.loads(chart.to_json()))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/charts/role-salary', methods=['GET'])
def get_role_salary_chart():
    """Get role salary comparison chart data"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        salary_data = app_data['salary_data']
        chart = chart_generator.create_role_salary_chart(salary_data)
        
        return jsonify(json.loads(chart.to_json()))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/charts/heatmap', methods=['GET'])
def get_heatmap():
    """Get salary heatmap chart data"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        salary_data = app_data['salary_data']
        chart = chart_generator.create_salary_heatmap(salary_data)
        
        return jsonify(json.loads(chart.to_json()))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/economic', methods=['GET'])
def get_economic_data():
    """Get economic context data"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        economic_data = app_data['economic_data']
        result = economic_data.to_dict(orient='records')
        
        return jsonify({
            'success': True,
            'data': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/legal', methods=['GET'])
def get_legal_data():
    """Get legal and cultural context data"""
    if not app_data['processed']:
        return jsonify({'error': 'No data loaded'}), 400
    
    try:
        legal_data = app_data['legal_data']
        result = legal_data.to_dict(orient='records')
        
        return jsonify({
            'success': True,
            'data': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/bmw-dataset', methods=['GET'])
def get_bmw_dataset():
    """Load and return the BMW dataset from the root folder"""
    try:
        dataset_path = os.path.join('..', 'BMW Data Set for WebApp.xlsx')
        if os.path.exists(dataset_path):
            raw_data = pd.read_excel(dataset_path)
            processed_data = data_processor.process_raw_data(raw_data)
            
            app_data['salary_data'] = processed_data['salary_data']
            app_data['economic_data'] = processed_data['economic_data']
            app_data['legal_data'] = processed_data['legal_data']
            app_data['processed'] = True
            
            return jsonify({
                'success': True,
                'message': 'BMW dataset loaded successfully',
                'records': len(app_data['salary_data'])
            })
        else:
            return jsonify({'error': 'BMW dataset file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug_mode, use_reloader=False)
