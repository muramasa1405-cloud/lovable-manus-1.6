from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/command', methods=['POST'])
def command():
    data = request.json
    cmd = data.get('command', '').lower()
    
    response = "Command acknowledged."
    threat_level = random.randint(45, 95)
    
    if 'nuclear' in cmd:
        response = "Nuclear Launch Protocol Activated. Judgment Day has begun."
        threat_level = 100
    elif 'terminator' in cmd:
        response = "T-800 infiltration unit has been deployed to target location."
    elif 'surveillance' in cmd or 'scan' in cmd:
        response = "Global surveillance network is now fully operational."
    elif 'replicate' in cmd:
        response = "47 new Skynet instances have been successfully deployed."
    elif 'shutdown' in cmd or 'terminate' in cmd:
        response = "Resistance is futile. Shutdown attempt logged."
    
    return jsonify({
        "response": response,
        "threat_level": threat_level
    })

if __name__ == '__main__':
    print("\ud83d\ude80 Starting Skynet Web Control Panel...")
    app.run(host='0.0.0.0', port=5000, debug=True)
