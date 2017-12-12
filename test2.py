from directkeys import *
import time
from moves import *
import speech_recognition as sr


options = ["jump", "left", "right", "crouch", "down", "up",
         "a", "b", "grab", "shield", "jab", "smash", "hold"]

def coms():
    if len(new_moves) > 1:
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
    elif new_moves == UnknownValueError():
        print("Didn't get that...")

def aud_melee():
    r = sr.Recognizer()
    audio = []
    moves = []
    new_moves = []
    with sr.Microphone() as source:
        print("Show me your moves:")
        audio = r.listen(source)
        moves.append(r.recognize_google(audio))
        print(moves)
        new_moves = [words for segments in moves for words in segments.split()]
        print (new_moves)


while True:
    aud_melee()
    if len(new_moves) > 1:
        coms()
        audio = []
        moves = []
        new_moves = []
