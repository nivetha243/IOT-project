import speech_recognition as sr
import requests

# Flask server URL

FLASK_SERVER_URL = 'http://127.0.0.1:5000'

# Function to send API request based on voice command
def execute_command(command):
    command = command.lower()  # Make the command lowercase for easier matching

    if "turn on tv" in command:
        print("Turning on the TV...")
        requests.post(f'{FLASK_SERVER_URL}/tv/on')
    elif "turn off tv" in command:
        print("Turning off the TV...")
        requests.post(f'{FLASK_SERVER_URL}/tv/off')
    elif "volume up" in command:
        print("Increasing TV volume...")
        requests.post(f'{FLASK_SERVER_URL}/tv/volume_up')
    elif "volume down" in command:
        print("Decreasing TV volume...")
        requests.post(f'{FLASK_SERVER_URL}/tv/volume_down')
    elif "turn on ac" in command:
        print("Turning on the AC...")
        requests.post(f'{FLASK_SERVER_URL}/ac/on')
    elif "turn off ac" in command:
        print("Turning off the AC...")
        requests.post(f'{FLASK_SERVER_URL}/ac/off')
    elif "temperature up" in command:
        print("Increasing AC temperature...")
        requests.post(f'{FLASK_SERVER_URL}/ac/temperature_up')
    elif "temperature down" in command:
        print("Decreasing AC temperature...")
        requests.post(f'{FLASK_SERVER_URL}/ac/temperature_down')
    else:
        print(f"Command not recognized: {command}")

# Main function to handle voice recognition
def recognize_voice():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for a command...")
        
        # Adjust for ambient noise and capture audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            execute_command(command)
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:
        recognize_voice()
