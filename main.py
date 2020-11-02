import twilio.rest # pip3 install twilio
import speech_recognition as sr # pip3 install SpeechRecognition pydub

recognizer = sr.Recognizer()

#Register on https://www.twilio.com/
sid = 'your_SID_ID'
auth_token = 'your_auth_token'

client = twilio.rest.Client(sid, auth_token)

with sr.Microphone() as source_audio: # pip3 install pyaudio, sudo apt install jackd2
    audio_data = recognizer.record(source_audio, duration=10) # records the voice for max 10 seconds
    text = recognizer.recognize_google(audio_data)
    print(text)
    to_send_or_not = input("Do you want to send this?") # Asks for if you want to send the message after checking the text

    if to_send_or_not.lower() == 'yes':
        message = client.messages.create(from_='your_generated_number_from_twilio', 
                                body= text, 
                                to='recipent_number')
    elif to_send_or_not.lower() == 'no':
        print("Exiting the program")
        exit()
    else:
        print('Something went wrong')
        exit()
