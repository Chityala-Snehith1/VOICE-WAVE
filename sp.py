import pyttsx3
import smtplib
import speech_recognition as sr
from email.message import EmailMessage

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('\nSpeak! I am listening...')
            voice_input = recognizer.listen(source)
            info = recognizer.recognize_google(voice_input).lower()
            print(info)
            return info
    except Exception as e:
        print("\nError in interpreting your voice! Please try again later.")
        print(f"Exception: {e}")
        return 0

def send_email(receiver, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('voicewaveproject@gmail.com', 'mjellbjjvyvmadbg')

        email = EmailMessage()
        email['From'] = 'voicewaveproject@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)

        server.send_message(email)
        server.quit()
        print("\nMail sent successfully!")
        speak('Your email is sent successfully!')
    except Exception as e:
        print("\nError sending email. Check your Gmail security settings and network connectivity.")
        print(f"Exception: {e}")

def main():
    print("\nWelcome to the Email Bot!\n")

    print("Who would you like to send the email to? (vijay/friend/dark):")
    speak('Who would you like to send the email to?')
    recipient_name = get_info()

    email_list = {
        'vijay': 'snehith.first@gmail.com',
        'fry': 'jnihanthreddy@gmail.com',
        'dark': 'friend@gmail.com'
    }

    if recipient_name not in email_list:
        print("Invalid recipient name. Please choose from 'vijay', 'dark', or 'friend'.")
        return

    receiver = email_list[recipient_name]
    print(f"Receiver email address: {receiver}")

    print("\nEnter the subject of your email:")
    speak('Enter the subject of your email')
    subject = get_info()

    print("\nEnter the body of your email:")
    speak('Enter the body of your email')
    body = get_info()

    print("\nSending email...")
    send_email(receiver, subject, body)

    #print("\nDo you want to send another email? (yes/no):")
   # speak('Do you want to send another email?')
   # send_again = get_info()
   # if 'yes' in send_again:
      #  main()

if __name__ == "__main__":
    main()
