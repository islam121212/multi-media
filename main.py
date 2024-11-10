import pyttsx3
import random
import time
import requests
from datetime import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
pitch = 1.0

random_phrases = [
    "Keep pushing forward!",
    "Learning never stops.",
    "Stay positive and strong.",
    "Success is a journey, not a destination."
]

favorite_phrases = []

def greet_user():
    name = input("What's your name? ")
    hour = datetime.now().hour
    if hour < 12:
        greeting = f"Good morning, {name}!"
    elif 12 <= hour < 18:
        greeting = f"Good afternoon, {name}!"
    else:
        greeting = f"Good evening, {name}!"
    
    engine.say(greeting)
    engine.runAndWait()

def change_voice():
    global voices
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name}")
    
    choice = int(input("Select a voice by number: "))
    if 0 <= choice < len(voices):
        engine.setProperty('voice', voices[choice].id)
        engine.say(f"Voice changed to {voices[choice].name}.")
        engine.runAndWait()
    else:
        print("Invalid choice.")

def change_pitch():
    global pitch
    pitch = float(input("Enter the new pitch level (e.g., 0.5 for low, 2.0 for high): "))
    engine.say(f"Pitch level changed to {pitch}.")
    engine.runAndWait()

def change_speed():
    speed = int(input("Enter the new speech rate (words per minute): "))
    engine.setProperty('rate', speed)
    engine.say(f"Speech rate changed to {speed} words per minute.")
    engine.runAndWait()

def set_timer():
    seconds = int(input("Enter time in seconds to wait before speaking: "))
    time.sleep(seconds)
    engine.say("Time's up!")
    engine.runAndWait()

def read_from_file():
    file_path = input("Enter the full path of the text file: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Reading file content:\n", content)
            engine.say(content)
            engine.runAndWait()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def auto_random_speech():
    interval = int(input("Enter interval time in seconds for random speech: "))
    while True:
        phrase = random.choice(random_phrases)
        engine.say(phrase)
        engine.runAndWait()
        time.sleep(interval)

def repeat_phrase():
    phrase = input("Enter the phrase you want to repeat: ")
    times = int(input("How many times do you want to repeat it? "))
    for _ in range(times):
        engine.say(phrase)
        engine.runAndWait()

def save_favorite_phrase():
    phrase = input("Enter the phrase you want to save as favorite: ")
    favorite_phrases.append(phrase)
    print(f"Phrase '{phrase}' has been saved as a favorite.")

def retrieve_favorite_phrases():
    if favorite_phrases:
        print("Favorite Phrases:")
        for phrase in favorite_phrases:
            print(f"- {phrase}")
    else:
        print("No favorite phrases saved.")

def read_favorite_phrases():
    if favorite_phrases:
        print("Reading favorite phrases:")
        for phrase in favorite_phrases:
            engine.say(phrase)
            engine.runAndWait()
    else:
        print("No favorite phrases saved.")

def read_from_url():
    url = input("Enter the URL of the text you want to read: ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        print("Reading content from URL:\n", content)
        engine.say(content)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred: {e}")

def show_info():
    print("Text-to-Speech Program")
    print("Developed by Doctor Ahmed Sayed Salama")
    print("Version 1.1")
    print("This program allows you to convert text to speech and offers various functionalities.")
    print("Features:")
    print("- Greet the user based on the time of day.")
    print("- Change voice and pitch of the speech.")
    print("- Change speech speed dynamically.")
    print("- Read text from a file.")
    print("- Speak random phrases at set intervals.")
    print("- Repeat a specific phrase multiple times.")
    print("- Save and retrieve favorite phrases.")
    print("- Read favorite phrases aloud.")
    print("- Read text content from a URL.")
    print("- Display program information.")

def main_menu():
    while True:
        print("\nOptions:")
        print("1. Greet User")
        print("2. Change Voice")
        print("3. Change Pitch")
        print("4. Change Speed")
        print("5. Set Timer to Speak")
        print("6. Read from File")
        print("7. Start Auto Random Speech")
        print("8. Repeat a Phrase")
        print("9. Save Favorite Phrase")
        print("10. Retrieve Favorite Phrases")
        print("11. Read Favorite Phrases")
        print("12. Read from URL")
        print("13. Show Program Info")
        print("14. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            greet_user()
        elif choice == '2':
            change_voice()
        elif choice == '3':
            change_pitch()
        elif choice == '4':
            change_speed()
        elif choice == '5':
            set_timer()
        elif choice == '6':
            read_from_file()
        elif choice == '7':
            auto_random_speech()
        elif choice == '8':
            repeat_phrase()
        elif choice == '9':
            save_favorite_phrase()
        elif choice == '10':
            retrieve_favorite_phrases()
        elif choice == '11':
            read_favorite_phrases()
        elif choice == '12':
            read_from_url()
        elif choice == '13':
            show_info()
        elif choice == '14':
            time.sleep(1)
            engine.say("Goodbye Doctor Ahmed Sayed Salama!")
            engine.runAndWait()
            time.sleep(0.5)
            print("Goodbye Doctor Ahmed Sayed Salama!")
            break
        else:
            print("Invalid choice, please try again.")

main_menu()