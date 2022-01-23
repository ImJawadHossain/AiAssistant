import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui
import smtplib
from email.message import EmailMessage
import webbrowser
from time import sleep
import os

gmail = os.environ.get("ine")
password = os.environ.get("password")

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey google' in command:
                command = command.replace('hey google', '')
                print(command)
    except:
        pass
    return command

def run_google():
    command = take_command()
    print(command)

    if 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'your name' in command:
        talk('my name is google assistant. I\'m created by md jawad hossain')
        print('my name is google assistant. I\'m created by md jawad hossain')

    elif 'create you' in command:
        talk('I\'m created by md jawad hossain')
        print('I\'m created by md jawad hossain')




    elif 'site' in command:
        print('which site you want to go?')
        talk('which site you want to go?')
        site = take_command()
        print('opening', site)
        talk('opening')
        talk(site)
        webbrowser.open('https://'+site)




    elif 'image to text' in command:
        print('whom image you want to create image to text')
        talk('whom image you want to create image to text')
        iname = take_command()
        print(iname)
        talk('creating Image to text')
        print('creating', iname, 'Image to text')
        link = {
            'jawad': 'jawad.png',
            'javed': 'jawad.png',
            'java 8': 'jawad.png',
            'jaat': 'jawad.png',
            'riyan': 'riyan.png',
            'ramayan': 'riyan.png',
            'tanvir': 'riyan.png',
            'pahad': 'forhad.png',
            'fahad': 'forhad.png',
            'forhad': 'forhad.png',
            'forehead': 'forhad.png',
            'download': 'download.png'

        }
        lin = link[iname]
        pywhatkit.image_to_ascii_art(lin, iname+'.txt')
        sleep(1)
        print('The image has been created successfully.\n you can see it from:::\nfile:///C:/Users/Md%20Jawad%20Hossain/PycharmProjects/chatbot2/'+iname+'.txt', '\nthis location.')
        talk('The image has been created successfully.you can see it from this location.')






    elif 'send' in command:
        def sent_email(receiver, subject, body):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail, password)
            email = EmailMessage()
            email['From'] = gmail
            email['To'] = receiver
            email['Subject'] = subject
            email.set_content(body)
            server.send_message(email)

        email_list = {
            'jawad': 'jawadsgs3@gmail.com',
            'sath': 'jawadsgs3@gmail.com',
            'aahat': 'jawadsgs3@gmail.com',
            'jorhat': 'jawadsgs3@gmail.com',
            'java 8': 'jawadsgs3@gmail.com',
            'javed': 'jawadsg3@gmail.com',
            'chat': 'jawadsg3@gmail.com',
            'jaat': 'jawadsg3@gmail.com',
            'tanvir': 'riyantanvir002@gmail.com',
            'riyan': 'riyantanvir002@gmail.com',
            'tuhin': 'mdforhad@gmail.com',
            'forhad': 'mdforhadul@gmail.com',
            'south': 'jawadsgs3@gmail.com'
        }

        def get_email_info():
            print('to whom you want to send email?')
            talk('to whom you want to send email?')
            name = take_command()
            print(name)
            receiver = email_list[name]
            print(receiver)
            print('What is the subject in your email?')
            talk('What is the subject in your email?')
            subject = take_command()
            print(subject)
            print('what do you want to send?')
            talk('what do you want to send?')
            body = take_command()
            print(body)
            print('Is that correct?')
            print('\n\nFrom :',gmail,' \n', 'To :', receiver, '\n Subject: ', subject, '\nBody :', body, '\n\n' )
            talk('Is that correct?')
            correct = take_command()
            if 'yes' in correct:
                sent_email(receiver, subject, body)
                print('Hey jawad . Your email is successfully sent to him')
                talk('Hey jawad . Your email is successfully sent to him')
                print('Do you want to send more email?')
                talk('Do you want to send more email?')
                send_more = take_command()
                if 'yes' in send_more:
                    get_email_info()
                if 'no' in send_more:
                    print('Ok. I ll be there when  you call me ')
                    talk('Ok. I ll be there when you call me.')
            if 'no' in correct:
                print('ok. I don\'t send the the email.')
                talk('ok. I don\'t send the the email.')
                print('Do you want to send email again to anyone?')
                talk('Do you want to send email again to anyone?')
                send_more = take_command()
                if 'yes' in send_more:
                    get_email_info()
                if 'no' in send_more:
                    print('Okey')
                    talk('Okey')

        get_email_info()





    elif 'you do' in command:
        talk('I\'m doing anything for you.')
        print('I\'m doing anything for you.')

    elif 'thank you' in command:
        talk('you\'re most welcome')
        print('you\'re most welcome')

    elif 'how are' in command:
        talk('im feeling happy when you talk to me. by the way, and you?')
        print('im feeling happy when you talk to me.by the way, and you?')

    elif 'how about you ' in command:
        talk('im feeling happy when you talk to me. by the way, and you?')
        print('im feeling happy when you talk to me.by the way, and you?')

    elif 'thanks' in command:
        talk('you\'re most welcome')
        print('you\'re most welcome')

    elif 'siri' in command:
        talk('Siri is a virtual assistant that is part of Apple Inc. .she is very intelligent like me!')
        print('Siri is a virtual assistant that is part of Apple Inc. .she is very intelligent like me!')

    elif 'ok' in command:
        talk(' ')
        print(' ')

    elif 'fine' in command:
        talk(' ')
        print(' ')

    elif 'weather' in command:
        pyautogui.hotkey('win', 's')
        pyautogui.typewrite(command)
        pyautogui.press('enter')

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what' in command:
        perso = command.replace('what', '')
        inf = wikipedia.summary(perso, 1)
        print(inf)
        talk(inf)

    elif 'date' in command:
        talk('sorry, I have a headache')
        print('sorry, I have a headache')

    elif 'you single' in command:
        talk('I am in a relationship with wifi')
        print('I am in a relationship with wifi')

    elif 'open' in command:
        a = command.replace('open', '')
        print('opening', a)
        talk('opening')
        pyautogui.hotkey('win', 's')
        pyautogui.typewrite(a)
        pyautogui.press('enter')

    elif 'your name' in command:
        talk('my name is google assistant. I\'m created by md jawad hossain')
        print('I am in a relationship with wifi')

    else:
        print('I find it to google')
        talk('I find it to google')
        webbrowser.open('https://www.google.com/search?q=' + command)


while True:
    run_google()
