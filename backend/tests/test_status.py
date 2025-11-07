import os
import importlib.util

# Load the app module directly from file to avoid import path issues during tests
app_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app.py'))
spec = importlib.util.spec_from_file_location('app_module', app_file)
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)
import werkzeug
if not hasattr(werkzeug, "__version__"):
    # Provide a compatible __version__ attribute for Werkzeug when missing
    werkzeug.__version__ = "3.1.3"


def test_status_endpoint():
    client = app_module.app.test_client()
    resp = client.get('/api/status')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['status'] == 'ok'
