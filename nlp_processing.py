# import spacy

# nlp = spacy.load("en_core_web_sm")

# def process_command(command):
#     doc = nlp(command)

#     device = None
#     action = None
#     value = None

#     # Extract relevant commands for controlling devices
#     if "AC" in command or "air conditioner" in command:
#         device = "AC"
#         if "increase" in command or "set" in command:
#             action = "set_temperature"
#             # Extract temperature from text
#             for token in doc:
#                 if token.like_num:
#                     value = token.text
#     elif "TV" in command:
#         device = "TV"
#         if "turn on" in command:
#             action = "power_on"
#         elif "turn off" in command:
#             action = "power_off"

#     return device, action, value
# nlp_processing.py

def process_command(command):
    command = command.lower()

    # Example logic to process command
    if "tv" in command:
        device = "tv"
        if "on" in command:
            action = "on"
        elif "off" in command:
            action = "off"
        elif "volume up" in command:
            action = "volume_up"
        elif "volume down" in command:
            action = "volume_down"
        else:
            action = None
        value = None
    elif "ac" in command:
        device = "ac"
        if "on" in command:
            action = "on"
        elif "off" in command:
            action = "off"
        elif "temperature up" in command:
            action = "temperature_up"
        elif "temperature down" in command:
            action = "temperature_down"
        else:
            action = None
        value = None
    else:
        device = None
        action = None
        value = None

    return device, action, value
