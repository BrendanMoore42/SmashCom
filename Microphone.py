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
moves = ["jump", "left", "right", "crouch", "down", "up",
         "a", "b", "grab", "shield", "jab", "smash", "hold"]



r = sr.Recognizer()

r.pause_threshold = 1.0
r.phrase_threshold = 1.0
r.non_speaking_duration = 0.35

while True:
    with sr.Microphone() as source:
        print("Say a move:")
        audio = r.listen(source)
        try:
            if r.recognize_google(audio) == "jump":
                print("You tried to {}".format(r.recognize_google(audio)))
                jump()
            elif r.recognize_google(audio) == "shine" or r.recognize_google(audio) == "down b":
                print("You tried to {}".format(r.recognize_google(audio)))
                shine()
            elif r.recognize_google(audio) == "left":
                print("You tried to go {}".format(r.recognize_google(audio)))
                left()
            elif r.recognize_google(audio) == "right":
                print("You tried to go {}".format(r.recognize_google(audio)))
                right()
            elif r.recognize_google(audio) == "crouch" or r.recognize_google(audio) == "down":
                print("You tried to {}".format(r.recognize_google(audio)))
                crouch()
            elif r.recognize_google(audio) == "Jab" or r.recognize_google(audio)== "a":
                print("You tried to {}".format(r.recognize_google(audio)))
                jab()
            elif r.recognize_google(audio) == "double Jab":
                print("You tried to {}".format(r.recognize_google(audio)))
                djab()
            elif r.recognize_google(audio) == "Shield":
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
            elif r.recognize_google(audio) == "up":
                print("You tried to {}".format(r.recognize_google(audio)))
                up()
            else:
                print("You said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

