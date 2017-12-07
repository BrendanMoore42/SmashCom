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

for i in list(range(2))[::-1]:
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

def mic_on():
    with sr.Microphone() as source:
        print ("Holy shit chill calibrating")
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say a move:")
        audio = r.listen(source)

r = sr.Recognizer()

# r.pause_threshold = 1.0
# r.phrase_threshold = 1.0
# r.non_speaking_duration = 0.35

moves = []
while True:
    # with sr.Microphone() as source:
    #     # print("Holy shit chill calibrating")
    #     # r.adjust_for_ambient_noise(source, duration=5)
    #     print("Say a move:")
    #     audio = r.listen(source)
    with sr.Microphone() as source:
        print("Show me your moves:")
        audio = r.listen(source)
        moves.append(r.recognize_google(audio))
        print(moves)
        new_moves = [words for segments in moves for words in segments.split()]
        print(new_moves)
        try:
            if "jump" in new_moves:
                jump()
            elif "left" in new_moves:
                left()
            else:
                print("You said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        audio = []
        moves = []
        new_moves = []




