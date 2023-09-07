import PyPDF2
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voices", voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1  # used to continue listening
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        speak("say again please......")
        return "none"
    query=query.lower()
    return query



def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning sir")
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
    elif hour > 12 and hour < 18:
        speak("Good Afternoon sir")
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
    else:
        speak("Good Evening sir")
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

def pdf_reader():
    book1 = open(f"D:\\My Projects\\Book reader\\Books\\{book}.pdf", "rb")
    pdfReader = PyPDF2.PdfReader(book1)
    total_pages = len(pdfReader.pages)

    speak(f"Total number of pages in this book are {total_pages}")

    speak("Please enter the page number you want to read:")
    pg = int(takecommand().lower())

    if pg < 1 or pg > total_pages:
        speak("Invalid page number")
        return

    page = pdfReader.pages[pg - 1]
    text = page.extract_text()
    speak(text)

if __name__ == "__main__":
    wish()
    speak("which book do you want to read sir ")
    book=takecommand()
    pdf_reader()


