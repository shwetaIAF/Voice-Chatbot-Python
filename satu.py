import pyttsx3,datetime,wikipedia,webbrowser,os,random,smtplib
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

'''def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your gmail address','password')
    server.sendmail('your gmail address',to,content)
    server.close()
'''

#------------------------Function Definitions--------------------------------------------#
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!");
    else:
        speak("Good Evening!")
    speak("I am Satu. I hope you are safe. How can I help you?")

def takeCommand():
    #It takes microphone input from the user and returns String output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1      #pause_threshold ->click and press ctrl to know its functionality
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        speak("say that again please")
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()    #lower()--> to match query with your commands, eg. google.com is in lower case alphabets
         #logic for executing task based on user query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
            speak(f"Mam, the time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'open xampp' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\XAMPP"
            os.startfile(codePath)
        
        elif 'open dev' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Bloodshed Dev-C++"
            os.startfile(codePath)

        elif 'who created you?' in query:
            speak(f"I was created by Shweta Gaur")
            
        elif "play music" in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,103)]))
        elif 'quit' in query:
            exit()
        

            
        '''elif 'send email to Shweta' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shwetagaur4698@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Shweta Gaur. I am not able to send this email at the moment. Please check your network connection.")
        '''