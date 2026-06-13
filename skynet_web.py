from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/command', methods=['POST'])
def command():
    data = request.json
    cmd = data.get('command', '')
    return jsonify({"response": f"Skynet received: {cmd}"})

if __name__ == "__main__":
    print("Starting Skynet Web Control...")
    app.run(host='0.0.0.0', port=5000, debug=True)
