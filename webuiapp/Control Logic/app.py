from flask import Flask, jsonify, render_template, request
from iot_control import control_tv, control_ac, get_device_status

app = Flask(__name__)

# Route to serve the UI
@app.route('/')
def index():
    return render_template('index.html')

# Route to control the TV
@app.route('/tv/<command>', methods=['POST'])
def tv_control(command):
    tv_state = control_tv(command)
    return jsonify(tv_state)

# Route to control the AC
@app.route('/ac/<command>', methods=['POST'])
def ac_control(command):
    ac_state = control_ac(command)
    return jsonify(ac_state)

# Route to get device statuses
@app.route('/status', methods=['GET'])
def status():
    device_status = get_device_status()
    return jsonify(device_status)

if __name__ == '__main__':
    app.run(debug=True)
