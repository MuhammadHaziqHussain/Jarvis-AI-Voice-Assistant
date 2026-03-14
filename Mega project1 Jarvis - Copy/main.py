import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi='add your own key'
def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def aiprocess(command):
    client=OpenAI(
    api_key='add your own key',
    )
    completion=client.chat.completions.create(
        model='gpt-5-nano',
        messages=[
            {'role':'system','content':'You are a virtual assistant named jarvis skilled in general tasks lie Alexa and google cloud.Give short but complete answers'},
            {'role':'user','content':command}

        ]
    )
    return completion.choices[0].message.content
def processcommand(c):
    if 'open google' in c.lower():
        webbrowser.open('https://google.com')
        speak('opening google')
    elif 'open facebook' in c.lower():
        webbrowser.open('https://facebook.com')
        speak('opening facebook')
    elif 'open youtube' in c.lower():
        speak('opening youtube')
        webbrowser.open('https://youtube.com')
    elif 'open linkedin' in c.lower():
        speak('opening linkedin')
        webbrowser.open('https://linkedin.com')
    elif 'open gmail' in c.lower():
        speak('opening gmail')
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    elif c.lower().startswith('play'):
        song=c.lower()[5:].strip()
        if song in musiclibrary.music:
            speak(f'Playing{song}')
            webbrowser.open(musiclibrary.music[song])
    elif 'news' in c.lower():
        r=requests.get('https://newsdata.io/api/1/latest?apikey=pub_5fe8011463d645418d39582f9c3924db&country=pk')
        if r.status_code==200:
            data=r.json()
            articles=data.get('results',[])
            for i,article in enumerate(articles,start=1):
                speak(f'news number{i}')
                speak(article['title'])
                i+=1
    else:
        output=aiprocess(c)
        speak(output)


if __name__=='__main__':
    speak('Initializing Jarvis....')
    while True:
        #listen for the wake wrd Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()

        print('Recognizing...')
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word= r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("How can I help you")
                #listen for command
                with sr.Microphone() as source:
                    print("How can I help you....")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
