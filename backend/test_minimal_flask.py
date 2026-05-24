from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def check_route():
    return jsonify({'status': 'working', 'message': 'Flask is running!'})

@app.route('/')
def home():
    return 'Minimal Flask App - Working!'

def test():
    """Test that the minimal Flask app responds correctly."""
    with app.test_client() as client:
        resp = client.get('/test')
        assert resp.status_code == 200
        data = resp.get_json()
        assert data['status'] == 'working'

        resp = client.get('/')
        assert resp.status_code == 200

if __name__ == '__main__':
    print("=" * 60)
    print("STARTING MINIMAL FLASK APP")
    print("=" * 60)
    print("If you see 'Running on http://127.0.0.1:5001', test with:")
    print("  curl http://localhost:5001/")
    print("  curl http://localhost:5001/test")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5001, debug=False, use_reloader=False)
