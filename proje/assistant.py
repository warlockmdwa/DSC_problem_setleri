import speech_recognition as sr
import pyttsx3
from tkinter import *
import smtplib
import pywhatkit
import datetime
import wikipedia
import webbrowser
from termcolor import colored
from pyfiglet import figlet_format

print((colored(figlet_format("Virtual Assistant\nAdam", font='standard'), color="yellow")))


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')



#Yazilan textleri sese ceviriyoruz burada
def talk(text):
    engine.say(text)
    engine.runAndWait()


#Sesli Komut fonksiyonumuz
def command():
        try:
            recog = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recog.listen(source)
                statement = recog.recognize_google(audio)

            if "Adam" in statement:
                talk(statement)
                statement = statement.replace('Adam', '')
                print(statement)

        except Exception as e:
            print(e)
            print("I cannot recognize your voice")
            return "None"
        return statement



##  E-MAIL GONDERICI  ###

def send_message():
    address_info = address.get()
    email_body_info = email_body.get()
    print(address_info,email_body_info)

    #Buraya e-posta adresinizi ve sifrenizi girin (dusuk guvenlikli bir hesap olsun lutfen)
    send_email =""
    send_password = ""

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(send_email,send_password)
    print("LOGIN SUCCES")

    server.sendmail(send_email,address_info,email_body_info)
    print("MESSAGE GONE")

    address_entry.delete(0,END)
    email_body_entry.delete(0,END)



app = Tk()
app.geometry("600x400")

app.title("ADAM E-MAIL SENDER")

heading = Label(text="VIRTUAL ASSISTANT E-MAIL SENDING APP",
                bg="black",fg="white",
                font="12",width="500",height="3")
heading.pack()

address_field = Label(text="ADDRESS: ")
email_body_field = Label(text="MESSAGE: ")

address_field.place(x=155,y=80)
email_body_field.place(x=155,y=150)

address = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable = address, width="30")
email_body_entry = Entry(textvariable=email_body,width="30")

address_entry.place(x=155,y=110)
email_body_entry.place(x=155,y=190)

button = Button(app,text="SEND MESSAGE",
                command=send_message,width="30",
                height="2",bg="black",fg="white")

button.place(x=155,y=220)






###     Sesli Komutlar    ####


def run():
    commandIt = command()
    print(commandIt)

    #Youtube de muzik ve video oynatmak icin
    if 'play' in commandIt or "music" in commandIt:
        talk('now playing'+commandIt.replace("play",''))
        pywhatkit.playonyt(commandIt)



    elif "who are you" in commandIt:
        talk("i am your virtual assistant adam"+commandIt.replace("who are you",''))
        print(talk)


    #E-posta islemleri
    elif "send message" in commandIt:
        try:
            send_message(mainloop())
        except Exception as e:
            print(e)
            return "None"
        return send_message()




    elif "hello" in commandIt or 'hi Adam' in commandIt:
        talk("Hello there")
        print("Hello there!")


    #Kisa wikipedia bilgileri
    elif "what is" in commandIt or 'Wikipedia' in commandIt:
        info = wikipedia.summary(commandIt, 2)
        print(info,'\n')
        talk(info)


    #Arama motoru
    elif "search" in commandIt:
        search = webbrowser.open_new_tab(commandIt.replace("search", ''))
        talk(search)
        print(search)


    #Google kisa yolu
    elif "open Google" in commandIt:
        webbrowser.open_new_tab("https://www.google.com")
        talk("As you wish")
        print("As you wish")


    #Stackoverflow kisa yolu
    elif "stack overflow" in commandIt:
        search = webbrowser.open("stackoverflow.com",commandIt)
        talk(search)
        print(search)


    #Zaman bildirimi
    elif 'time' in commandIt:
        time = datetime.datetime.now().strftime('%H:%M:%A:%d:%B:%Y')+commandIt.replace('time','')
        hour = int(datetime.datetime.now().hour)


        if hour >= 6 and hour < 12:
            talk("Good morning!")
            print('Good morning')

        elif hour >= 12 and hour < 18:
            talk("Good afternoon!")
            print("Good afternoon!")

        elif hour >=18 and hour < 23:
            talk("Good evening")
            print("Good evening!")

        else:
            talk("Good night!")
            print("Good night!")

        talk("Current time is: " + time)
        print("Current time is: "+time)


    #sonlandirmak icin
    elif "that's enough" in commandIt:
        talk("Bye")
        print("Adios...")
        quit()



while True:
    run()


