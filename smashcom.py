#!/usr/bin/python3
"""
author: @brendanmoore42
date: Jan 11, 2019

SmashComm: Control the game.
"""
from directkeys import *
import time
import sys
import keyboard
from moves import *
import speech_recognition as sr

#extra modifiers for next update
#one button options
#options = ["jump", "left", "right",
#          "crouch", "down", "up",
#           "a", "b", "grab", "shield",
#           "jab", "smash"]



#instantiate Recognizer class
r = sr.Recognizer()

moves = []
go = sp


version = '1.0.5'

def lets_go():
    print('Press "r" to record.')
    while True:
        try:
            if keyboard.is_pressed('r'):
                show_me_your_moves()
                break
        except:
            break
    lets_go()


def show_me_your_moves():
    with sr.Microphone() as source:
        audio = []
        moves = []
        new_moves = []
        try:
            print("Show me your moves! ")
            #microphone is listening
            audio = r.listen(source)
            moves.append(r.recognize_google(audio))
            # run main fn
            execute_moves(moves=moves)
        except:
            pass

lets_go()