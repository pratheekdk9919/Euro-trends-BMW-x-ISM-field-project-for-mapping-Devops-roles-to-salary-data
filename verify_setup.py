"""
Verification Script for BMW DevOps Dashboard
Checks if all required components are properly set up
"""

import sys
import os
import subprocess
from pathlib import Path

def check_section(title):
    """Print section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)

def check_python_version():
    """Check Python version"""
    check_section("Python Version")
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    if version.major == 3 and version.minor >= 13:
        print("✓ Python version is compatible (3.13+)")
        return True
    else:
        print("✗ Python 3.13+ required")
        return False

def check_packages():
    """Check required Python packages"""
    check_section("Python Packages")
    required = {
        'flask': '2.3.2',
        'pandas': '2.3.0',
        'numpy': '2.3.1',
        'sklearn': '1.7.0',
        'plotly': '6.2.0',
        'flask_cors': '4.0.0',
        'openpyxl': '3.1.5'
    }
    
    all_installed = True
    for package, expected_version in required.items():
        try:
            if package == 'sklearn':
                import sklearn
                version = sklearn.__version__
                package_name = 'scikit-learn'
            else:
                module = __import__(package)
                version = module.__version__
                package_name = package
            
            print(f"✓ {package_name} {version}")
        except ImportError:
            print(f"✗ {package} NOT INSTALLED")
            all_installed = False
        except AttributeError:
            print(f"✓ {package} (version unknown)")
    
    return all_installed

def check_files():
    """Check critical files exist"""
    check_section("Critical Files")
    
    # Backend files
    backend_files = [
        'backend/app.py',
        'backend/data_processor.py',
        'backend/forecasting.py',
        'backend/visualizations.py',
        'backend/utils.py',
        'backend/requirements.txt'
    ]
    
    # Frontend files
    frontend_files = [
        'frontend/src/App.tsx',
        'frontend/src/App.css',
        'frontend/package.json',
        'frontend/vite.config.ts',
        'frontend/tsconfig.json'
    ]
    
    # Dataset
    dataset_files = [
        '../BMW Data Set for WebApp.xlsx',
        'BMW Data Set for WebApp.xlsx'  # Try both locations
    ]
    
    all_files = backend_files + frontend_files
    all_exist = True
    
    for filepath in all_files:
        if os.path.exists(filepath):
            print(f"✓ {filepath}")
        else:
            print(f"✗ {filepath} MISSING")
            all_exist = False
    
    # Check dataset
    dataset_found = False
    for filepath in dataset_files:
        if os.path.exists(filepath):
            print(f"✓ Dataset found: {filepath}")
            dataset_found = True
            break
    
    if not dataset_found:
        print(f"✗ BMW Data Set for WebApp.xlsx NOT FOUND")
        all_exist = False
    
    return all_exist

def check_node():
    """Check Node.js installation"""
    check_section("Node.js & npm")
    try:
        node_version = subprocess.run(['node', '--version'], capture_output=True, text=True)
        npm_version = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        
        if node_version.returncode == 0:
            print(f"✓ Node.js {node_version.stdout.strip()}")
        else:
            print("✗ Node.js NOT FOUND")
            return False
        
        if npm_version.returncode == 0:
            print(f"✓ npm {npm_version.stdout.strip()}")
        else:
            print("✗ npm NOT FOUND")
            return False
        
        return True
    except FileNotFoundError:
        print("✗ Node.js/npm NOT INSTALLED")
        return False

def check_frontend_packages():
    """Check if frontend packages are installed"""
    check_section("Frontend Packages")
    
    node_modules = Path('frontend/node_modules')
    package_json = Path('frontend/package.json')
    
    if not package_json.exists():
        print("✗ frontend/package.json NOT FOUND")
        return False
    
    print(f"✓ package.json found")
    
    if node_modules.exists():
        # Count packages
        packages = list(node_modules.iterdir())
        print(f"✓ node_modules found ({len(packages)} packages)")
        
        # Check critical packages
        critical = ['react', 'react-dom', 'axios', 'plotly.js', 'typescript', 'vite']
        all_found = True
        for pkg in critical:
            pkg_path = node_modules / pkg
            if pkg_path.exists():
                print(f"  ✓ {pkg}")
            else:
                print(f"  ✗ {pkg} MISSING")
                all_found = False
        
        return all_found
    else:
        print("✗ node_modules NOT FOUND - run 'npm install --legacy-peer-deps'")
        return False

def check_backend_imports():
    """Test backend module imports"""
    check_section("Backend Module Imports")
    
    all_imported = True
    modules = [
        ('data_processor', 'DataProcessor'),
        ('forecasting', 'SalaryForecaster'),
        ('visualizations', 'ChartGenerator'),
        ('utils', 'format_currency')
    ]
    
    # Add backend to path
    sys.path.insert(0, 'backend')
    
    for module_name, class_name in modules:
        try:
            module = __import__(module_name)
            if hasattr(module, class_name):
                print(f"✓ {module_name}.{class_name}")
            else:
                print(f"✗ {module_name}.{class_name} NOT FOUND")
                all_imported = False
        except ImportError as e:
            print(f"✗ {module_name} IMPORT ERROR: {e}")
            all_imported = False
    
    return all_imported

def main():
    """Run all checks"""
    print("\n" + "="*60)
    print("  BMW DevOps Dashboard - Setup Verification")
    print("="*60)
    
    results = {
        'Python Version': check_python_version(),
        'Python Packages': check_packages(),
        'Critical Files': check_files(),
        'Node.js & npm': check_node(),
        'Frontend Packages': check_frontend_packages(),
        'Backend Imports': check_backend_imports()
    }
    
    # Summary
    check_section("Summary")
    all_passed = True
    for check, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status:10} {check}")
        if not passed:
            all_passed = False
    
    print("\n" + "="*60)
    if all_passed:
        print("  ✓ ALL CHECKS PASSED - Ready to run!")
        print("  Run: .\\START_APPLICATION.bat")
    else:
        print("  ✗ SOME CHECKS FAILED - Review errors above")
        print("  See SETUP_GUIDE.md for troubleshooting")
    print("="*60 + "\n")
    
    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())
