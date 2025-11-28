# import pyttsx3
# import speech_recognition as sr
# import webbrowser
# import datetime
# import pyjokes
# import wikipedia
# import random

# # -----------------------
# # Text-to-Speech Setup
# # -----------------------
# engine = pyttsx3.init()
# engine.setProperty('rate', 170)

# # ---- FEMALE GUJARATI/INDIAN VOICE SETUP ----
# voices = engine.getProperty("voices")
# for v in voices:
#     if (
#         "female" in v.name.lower()
#         or "zira" in v.name.lower()
#         or "heli" in v.id.lower()
#         or "india" in v.id.lower()
#         or "hindi" in v.name.lower()
#     ):
#         engine.setProperty("voice", v.id)
#         break


# def speak(text):
#     print("Assistant:", text)
#     engine.say(text)
#     engine.runAndWait()


# # -----------------------
# # Listen to Voice
# # -----------------------
# def voice_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)

#     try:
#         command = r.recognize_google(audio)
#         print("You said:", command)
#         return command.lower()

#     except sr.UnknownValueError:
#         speak("Sorry, I did not understand. Please type your command.")
#         return text_command()

#     except sr.RequestError:
#         speak("Speech service error. Type your command.")
#         return text_command()


# # -----------------------
# # Text Command
# # -----------------------
# def text_command():
#     return input("Type your command: ").lower()


# # -----------------------
# # Reminders
# # -----------------------
# reminders = []


# # -----------------------
# # Calculator
# # -----------------------
# def calculator(command):
#     try:
#         expr = command.replace("calculate", "").replace("what is", "")
#         result = eval(expr)
#         speak(f"The result is {result}")
#     except:
#         speak("Sorry, I cannot calculate that.")


# # -----------------------
# # MAIN ASSISTANT LOGIC
# # -----------------------
# def assistant(command):
#     # TIME
#     if "time" in command:
#         t = datetime.datetime.now().strftime("%H:%M:%S")
#         speak(f"The time is {t}")

#     # DATE
#     elif "date" in command:
#         d = datetime.datetime.now().strftime("%Y-%m-%d")
#         speak(f"Today's date is {d}")

#     # WIKIPEDIA
#     elif "wikipedia" in command:
#         speak("Searching Wikipedia...")
#         query = command.replace("wikipedia", "")
#         try:
#             result = wikipedia.summary(query, sentences=2)
#             speak(result)
#         except:
#             speak("No Wikipedia result found.")

#     # CALCULATE
#     elif "calculate" in command or "what is" in command:
#         calculator(command)

#     # OPEN GOOGLE
#     elif "open google" in command or "google kholo" in command:
#         speak("Opening Google")
#         webbrowser.open("https://www.google.com")

#     # OPEN YOUTUBE
#     elif "open youtube" in command or "youtube kholo" in command:
#         speak("Opening YouTube")
#         webbrowser.open("https://www.youtube.com")

#     # GITHUB
#     elif "github" in command:
#         speak("Opening GitHub")
#         webbrowser.open("https://www.github.com")

#     # GMAIL
#     elif "open gmail" in command:
#         speak("Opening Gmail")
#         webbrowser.open("https://mail.google.com")

#     # WHATSAPP
#     elif "whatsapp" in command:
#         speak("Opening WhatsApp Web")
#         webbrowser.open("https://web.whatsapp.com")

#     # WEATHER
#     elif "weather" in command:
#         city = command.replace("weather", "")
#         speak("Checking the weather")
#         webbrowser.open(f"https://www.google.com/search?q=weather+{city}")

#     # JOKES
#     elif "joke" in command or "majak" in command:
#         if "gujarati" in command or "guj" in command or "majak" in command:
#             guj_jokes = [
#                 "એક વાર મમ્મીએ પૂછ્યું: સ્કૂલ મોડું કેમ? બોલ્યો: ટીચર કહે છે કે મોડું આવે તો સ્ટેન્ડિંગ ઓવેશન મળે છે!",
#                 "પત્ની: બહાર ફરવા કેમ નથી લઈને જતા? પતિ: ચાલો, આજે બિલોના ચક્કર લગાડીએ!",
#                 "શિક્ષક: પાણી વગર જીવવું શક્ય છે? વિદ્યાર્થી: હા સર, બોટલનું પાણી પી જઈશું!",
#                 "મિત્ર: તું ખુશ કેમ છે? બીજો: બે દિવસથી મારી વાઈફ મારે બોલતી જ નથી!"
#             ]
#             speak(random.choice(guj_jokes))
#         else:
#             speak(pyjokes.get_joke())

#     # QUOTES
#     elif "motivate" in command or "quote" in command:
#         q = [
#             "Believe you can and you're halfway there.",
#             "Do something today that your future self will thank you for.",
#             "Dream big and dare to fail.",
#             "Push yourself because no one else will do it for you."
#         ]
#         speak(random.choice(q))

#     # SET REMINDER
#     elif "set reminder" in command:
#         reminder_text = command.replace("set reminder", "").strip()
#         reminders.append(reminder_text)
#         speak(f"Reminder added: {reminder_text}")

#     # SHOW REMINDERS
#     elif "show reminders" in command:
#         if reminders:
#             speak("Your reminders are:")
#             for i, r in enumerate(reminders, 1):
#                 speak(f"{i}: {r}")
#         else:
#             speak("No reminders found.")

#     # EXIT
#     elif "exit" in command or "bye" in command:
#         speak("Goodbye!")
#         exit()

#     else:
#         speak("I cannot do that yet.")


# # -----------------------
# # MAIN LOOP
# # -----------------------
# def main():
#     speak("Hello! I am your AI assistant. Speak or type commands.")

#     while True:
#         choice = input("Enter 'voice' or 'text': ").lower()

#         if choice == "voice" or choice == "v":
#             command = voice_command()
#         elif choice == "text" or choice == "t":
#             command = text_command()
#         else:
#             speak("Invalid choice.")
#             continue

#         assistant(command)


# # -----------------------
# # RUN PROGRAM
# # -----------------------
# if __name__ == "__main__":
#     main()































# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import datetime
# import webbrowser
# import wikipedia
# import pyjokes
# import random
# import pyttsx3

# app = Flask(__name__)
# CORS(app)

# # ------------ AI Assistant TTS ------------
# engine = pyttsx3.init()
# engine.setProperty('rate', 170)

# voices = engine.getProperty("voices")
# for v in voices:
#     if "female" in v.name.lower() or "india" in v.id.lower():
#         engine.setProperty("voice", v.id)
#         break

# def speak(text):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except:
#         pass


# # ------------ MAIN ASSISTANT FUNCTION ------------
# def assistant(command):
#     command = command.lower().strip()

#     # TIME
#     if "time" in command:
#         t = datetime.datetime.now().strftime("%H:%M:%S")
#         return f"The time is {t}"

#     # DATE
#     elif "date" in command:
#         d = datetime.datetime.now().strftime("%Y-%m-%d")
#         return f"Today's date is {d}"

#     # GOOGLE
#     elif "open google" in command or "google kholo" in command:
#         webbrowser.open("https://www.google.com")
#         return "Opening Google"

#     # YOUTUBE
#     elif "open youtube" in command or "youtube kholo" in command:
#         webbrowser.open("https://www.youtube.com")
#         return "Opening YouTube"

#     # WIKIPEDIA SEARCH
#     elif "wikipedia" in command:
#         speak("Searching Wikipedia...")
#         query = command.replace("wikipedia", "")
#         try:
#             info = wikipedia.summary(query, sentences=2)
#             return info
#         except:
#             return "No result found on Wikipedia."

#     # JOKE
#     elif "joke" in command or "majak" in command:
#         return pyjokes.get_joke()

#     # UNKNOWN COMMAND
#     else:
#         return "I cannot do that yet."


# # ------------ API ENDPOINT ------------
# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()

#     if not data or "message" not in data:
#         return jsonify({"reply": "Invalid request"}), 400

#     user_msg = data["message"]
#     reply = assistant(user_msg)

#     # Speak reply
#     speak(reply)

#     return jsonify({"reply": reply})


# # ------------ RUN SERVER ------------
# if __name__ == "__main__":
#     print("🚀 Server running on http://localhost:4000")
#     app.run(port=4000, debug=True)

























from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import webbrowser
import datetime
import wikipedia
import pyjokes
import random
import pyttsx3

app = Flask(__name__)
CORS(app)

# ------------ LOAD JSON COMMANDS ------------
with open("data.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)["commands"]

# ------------ AI Assistant TTS ------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
for v in voices:
    if "female" in v.name.lower() or "india" in v.id.lower():
        engine.setProperty("voice", v.id)
        break

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass


# ------------ SPECIAL ACTION FUNCTIONS ------------
def get_time():
    return f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}"

def get_date():
    return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"

def google_search(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return "Searching Google"

def calculator(text):
    try:
        expr = text.replace("calculate", "").replace("what is", "")
        return f"The result is {eval(expr)}"
    except:
        return "Invalid calculation."


# ------------ MAIN MATCHING ENGINE ------------
def match_command(user_msg):

    user_msg = user_msg.lower()

    for cmd in DATA:
        for key in cmd["keywords"]:

            if key in user_msg:

                # SIMPLE RESPONSE TYPE
                if "response" in cmd:
                    return cmd["response"]

                # ACTIONS (WEBSITE)
                if cmd.get("type") == "website":
                    webbrowser.open(cmd["action"])
                    return f"Opening {cmd['action']}"

                # SYSTEM ACTIONS
                if cmd.get("action") == "get_time":
                    return get_time()

                if cmd.get("action") == "get_date":
                    return get_date()

                if cmd.get("action") == "calculator":
                    return calculator(user_msg)

                if cmd.get("action") == "google_search":
                    query = user_msg.replace(key, "")
                    return google_search(query)

    # EXTRA fallback from your previous assistant:
    if "wikipedia" in user_msg:
        try:
            query = user_msg.replace("wikipedia", "")
            return wikipedia.summary(query, sentences=2)
        except:
            return "No result found on Wikipedia."

    return "I cannot do that yet."


# ------------ API ENDPOINT ------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Invalid request"}), 400

    user_msg = data["message"]

    reply = match_command(user_msg)

    speak(reply)

    return jsonify({"reply": reply})


# ------------ RUN SERVER ------------
if __name__ == "__main__":
    print("🚀 Server running on http://localhost:4000")
    app.run(port=4000, debug=True)
