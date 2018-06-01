import speech_recognition as sr


recognizer =  sr.Recognizer()
recognizer.energy_threshold = 100

def transcribe(audio_file='sample.wav'):
    sound = sr.AudioFile(audio_file)
    with sound as source:
        audio = recognizer.record(source)

    try:
        print (recognizer.recognize_google(audio))

    except sr.UnknownValueError:
        print ("Did not understand")


def listen_microphone():
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
    try:
        print("Speech Recognition thinks you said " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# transcribe()
listen_microphone()