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
r.pause_threshold = 1.0
r.phrase_threshold = 1.0
r.non_speaking_duration = 1.0
while True:
    with sr.Microphone() as source:
        print("Say a move:")
        audio = r.listen(source)
        aud_list = [audio]
        for w in aud_list:
            print ("word: ", aud_list)
