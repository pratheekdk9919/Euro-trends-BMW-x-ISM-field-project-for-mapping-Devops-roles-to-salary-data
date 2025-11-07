from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def test():
    return jsonify({'status': 'working', 'message': 'Flask is running!'})

@app.route('/')
def home():
    return 'Minimal Flask App - Working!'

if __name__ == '__main__':
    print("="*60)
    print("STARTING MINIMAL FLASK APP")
    print("="*60)
    print("If you see 'Running on http://127.0.0.1:5001', test with:")
    print("  curl http://localhost:5001/")
    print("  curl http://localhost:5001/test")
    print("="*60)
    app.run(host='0.0.0.0', port=5001, debug=False, use_reloader=False)
    print("Flask app.run() returned - this should not happen!")
