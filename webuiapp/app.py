from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulated states for the devices
tv_state = {
    "status": "off",
    "volume": 5
}

ac_state = {
    "status": "off",
    "temperature": 18
}

# Routes for TV commands
@app.route('/tv/<command>', methods=['POST'])
def tv_control(command):
    global tv_state
    if command == "on":
        tv_state['status'] = "on"
    elif command == "off":
        tv_state['status'] = "off"
    elif command == "volume_up":
        if tv_state['volume'] < 100:  # Maximum volume is 100
            tv_state['volume'] += 5
    elif command == "volume_down":
        if tv_state['volume'] > 0:  # Minimum volume is 0
            tv_state['volume'] -= 5
    return jsonify(tv_state)

# Routes for AC commands
@app.route('/ac/<command>', methods=['POST'])
def ac_control(command):
    global ac_state
    if command == "on":
        ac_state['status'] = "on"
    elif command == "off":
        ac_state['status'] = "off"
    elif command == "temperature_up":
        if ac_state['temperature'] < 30:
            ac_state['temperature'] += 1
    elif command == "temperature_down":
        if ac_state['temperature'] > 18:
            ac_state['temperature'] -= 1
    return jsonify(ac_state)
    
@app.route('/status', methods=['GET'])
def get_status():
    global tv_state, ac_state
    return jsonify({
        "tv": tv_state,
        "ac": ac_state
    })

# Home page
@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)
