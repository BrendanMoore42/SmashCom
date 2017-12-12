# get audio from the microphone

import speech_recognition as sr

r = sr.Recognizer()
moves = []
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
    moves.append(r.recognize_google(audio))
    print (moves)
    new_moves = [words for segments in moves for words in segments.split()] #Splits moves to a list/individual words
    print (new_moves)

try:
    if r.recognize_google(audio) == "Hello":
        print ("Hello!")
    else:
        print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))