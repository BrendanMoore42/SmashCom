from directkeys import *
import time
from moves import *
import speech_recognition as sr


options = ["jump", "left", "right", "crouch", "down", "up",
         "a", "b", "grab", "shield", "jab", "smash", "hold"]

r = sr.Recognizer()

moves = []
while True:
    with sr.Microphone() as source:
        print("Show me your moves:")
        audio = r.listen(source)
        moves.append(r.recognize_google(audio))
        print(moves)
        new_moves = [words for segments in moves for words in segments.split()]
        print(new_moves)
        try:
            for action in new_moves:
                if action == "jump":
                    jump()
                elif action == "laser":
                    laser()
                elif action == "double-laser":
                    shdl()
                elif action == "up":
                    up()
                elif action == "left":
                    left()
                elif action == "right":
                    right()
                elif action == "down" or action == "crouch":
                    crouch()
                elif action == "punch" or action == "Jab":
                    jab()
                elif action == "double" and action == "Jab":
                    djab()
                elif action == "Shield":
                    shield()
                elif action == "grab":
                    grab()
                elif action == "right smash":
                    Rsmash()
                elif action == "left smash":
                    Lsmash()
                elif action == "shine":
                    shine()
            else:
                print("You said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        audio = []
        moves = []
        new_moves = []
