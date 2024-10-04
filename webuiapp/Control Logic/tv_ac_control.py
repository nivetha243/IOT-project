import requests

BASE_URL = "http://127.0.0.1:5000"  # The URL of the Flask server

# TV control functions
def turn_on_tv():
    response = requests.post(f"{BASE_URL}/tv/on")
    return response.json()

def turn_off_tv():
    response = requests.post(f"{BASE_URL}/tv/off")
    return response.json()

def volume_up_tv():
    response = requests.post(f"{BASE_URL}/tv/volume_up")
    return response.json()

def volume_down_tv():
    response = requests.post(f"{BASE_URL}/tv/volume_down")
    return response.json()

# AC control functions
def turn_on_ac():
    response = requests.post(f"{BASE_URL}/ac/on")
    return response.json()

def turn_off_ac():
    response = requests.post(f"{BASE_URL}/ac/off")
    return response.json()

def temperature_up_ac():
    response = requests.post(f"{BASE_URL}/ac/temperature_up")
    return response.json()

def temperature_down_ac():
    response = requests.post(f"{BASE_URL}/ac/temperature_down")
    return response.json()
