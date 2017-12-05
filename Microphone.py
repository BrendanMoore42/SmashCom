import speech_recognition as sr
from directkeys import PressKey, ReleaseKey, A, B, X, Y, Z, START, UP, DOWN, LEFT, RIGHT, CUP, CD, CR, CL, L, R, DUP
import time
from moves import *


# # get audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Speak:")
#     audio = r.listen(source)
#
# try:
#     if r.recognize_google(audio) == "up smash":
#         print ("Great upsmash!!")
#     else:
#         print("You said " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))

for i in list(range(4))[::-1]:
    print (i+1)
    time.sleep(1)


#
# while True:
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print ("Say the move: ")
#         audio = r.listen(source)
#         new_audio = [audio]
#         for word in new_audio:
#             if word == moves:
#


# punch = ["punch", "jab", "a"]



r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say a move:")
        audio = r.listen(source)
        for word in list(audio):
            try:
                if r.recognize_google(audio) == "jump":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    jump()
                elif r.recognize_google(audio) == "shine":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    shine()
                elif r.recognize_google(audio) == "left":
                    print("You tried to go {}".format(r.recognize_google(audio)))
                    left()
                elif r.recognize_google(audio) == "right":
                    print("You tried to go {}".format(r.recognize_google(audio)))
                    right()
                elif r.recognize_google(audio) == "crouch":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    crouch()
                elif r.recognize_google(audio) == "jab" or r.recognize_google(audio)== "a":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    jab()
                elif r.recognize_google(audio) == "shield":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    shield()
                elif r.recognize_google(audio) == "grab":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    grab()
                elif r.recognize_google(audio) == "laser":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    laser()
                elif r.recognize_google(audio) == "left smash":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    Lsmash()
                elif r.recognize_google(audio) == "right smash":
                    print("You tried to {}".format(r.recognize_google(audio)))
                    Rsmash()
                else:
                    print("You said " + r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

