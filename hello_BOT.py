import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Say Fast...I have a train to catch')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello' in command:
                command=command.replace('hello','')
                talk(command)
                print('Search:'+command)
    except:
        pass
    return command

def run_hello():
    command=take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('party starting' +song)
        print('Playing...'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+time)
    elif 'wikipedia' or 'who' or 'where' or 'knowledge' or 'what' or 'search' in command:
        person=command.replace('wikipedia'or'who'or'where'or'knowledge'or'what'or'search','')
        if 'is' in command:
            person = command.replace('is','')
        elif 'are' in command:
            person = command.replace('are','')
        elif 'were' in command:
            person = command.replace('were','')
        elif 'was' in command:
            person = command.replace('was','')
        info = wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'do you want to go on a date with me' or 'how about a date with me' or 'what about a date' in command:
        talk('get lost i love someone')
    elif 'do you think i am ugly' or 'am i ugly' in command:
        talk('yes you are')
    elif 'you are bad' or 'you are the worst' in command:
        talk('i am as emotionless as my creator')
    elif 'joke' in command:
        if 'Do not' in command:
            talk('Ok')
        else:
            joker = pyjokes.get_joke()
            print(joker)
            talk(joker)
    else:
        talk('please say again')
        
        
while True:        
    run_hello()