# import paho.mqtt.client as mqtt
# import json

# def get_mqtt_config():
#     with open('config/mqtt_config.json') as config_file:
#         return json.load(config_file)

# def control_device(device, action, value=None):
#     config = get_mqtt_config()
#     broker = config['broker']
#     port = config['port']

#     client = mqtt.Client()
#     client.connect(broker, port)

#     if device == "AC":
#         if action == "set_temperature":
#             topic = "home/ac/temperature"
#             client.publish(topic, value)
#             print(f"AC temperature set to {value}°C")
#     elif device == "TV":
#         if action == "power_on":
#             topic = "home/tv/power"
#             client.publish(topic, "on")
#             print("TV turned on")
#         elif action == "power_off":
#             topic = "home/tv/power"
#             client.publish(topic, "off")
#             print("TV turned off")
    
#     client.disconnect()
# device_control.py

def control_device(device, action, value=None):
    if device == "tv":
        if action == "on":
            print("Turning on the TV...")
            # Add code to turn on TV
        elif action == "off":
            print("Turning off the TV...")
            # Add code to turn off TV
        elif action == "volume_up":
            print("Increasing TV volume...")
            # Add code to increase TV volume
        elif action == "volume_down":
            print("Decreasing TV volume...")
            # Add code to decrease TV volume
    elif device == "ac":
        if action == "on":
            print("Turning on the AC...")
            # Add code to turn on AC
        elif action == "off":
            print("Turning off the AC...")
            # Add code to turn off AC
        elif action == "temperature_up":
            print("Increasing AC temperature...")
            # Add code to increase AC temperature
        elif action == "temperature_down":
            print("Decreasing AC temperature...")
            # Add code to decrease AC temperature
    else:
        print("Unknown device or action.")
