import threading
def mouse():
    import time

    import cv2
    import mediapipe as mp
    import pyautogui
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]

            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))



            if (left[0].y - left[1].y) < 0.01:
                pyautogui.doubleClick()
                # pyautogui.click()
                # print("double Click")
                time.sleep(1)










        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)


#################################################

def jawad():

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

        elif 'visit' in command:
            website = command.replace('visit ', '')
            webbrowser.open('https://'+website)
            talk(website)




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




        elif 'type right' in command:
            type_text = command.replace('type right', '')
            pyautogui.typewrite(type_text)
            talk(type_text)

        elif "type write" in command:
            type_text = command.replace('type write', '')
            pyautogui.typewrite(type_text)
            talk(type_text)


        elif 'double click' in command:
            pyautogui.doubleClick()
            print('Double Clicked')


        elif 'scroll up' in command:
            pyautogui.press("pgup")
            print('Page Up')

        elif 'scroll down' in command:
            pyautogui.press("pgdn")
            print('Page Down')

        elif 'right click' in command:
            pyautogui.rightClick()
            talk('right clicked')
            print('Right clicked')

        elif 'left click' in command:
            pyautogui.click()
            talk('left clicked')
            print('Left clicked')



        elif 'minimise' in command:
            pyautogui.hotkey('win', 'down')
            talk('Window minimised.')
            print('Window minimised.')


        elif 'you do' in command:
            talk('I\'m doing anything for you.')
            print('I\'m doing anything for you.')

        elif 'close' in command:
            pyautogui.hotkey('alt', 'f4')
            talk('Window closed')
            print('Window closed')

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
            sleep(1.5)
            pyautogui.typewrite(command)
            sleep(0.5)
            pyautogui.press('enter')

        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'the time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)

        elif 'maximize' in command:
            pyautogui.hotkey('win', 'up')
            print("Window maximized")
            talk("Window maximized")

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
            sleep(1.5)
            pyautogui.typewrite(a)
            sleep(0.2)
            pyautogui.press('enter')

        elif 'your name' in command:
            talk('my name is Jawad assistant. I\'m created by md jawad hossain')
            print('I am in a relationship with wifi')

        else:
            print('I find it to google')
            talk('I find it to google')
            webbrowser.open('https://www.google.com/search?q=' + command)


    while True:

        try:
            run_google()
        except:
            pass



thread1 = threading.Thread(target=mouse)
thread2 = threading.Thread(target=jawad)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()


