
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

# Welcome message
speak("Hello! I am your voice assistant. How can I help you?")

# Main program
while True:

    command = listen()

    if "hello" in command:
        speak("Hello! Nice to meet you.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "search for" in command:
        topic = command.replace("search for", "").strip()

        if topic:
            speak("Searching for " + topic)
            webbrowser.open("https://www.google.com/search?q=" + topic.replace(" ", "+"))
        else:
            speak("Please tell me what you want to search for.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        break

    elif command:
        speak("Sorry, this command is not available.")
