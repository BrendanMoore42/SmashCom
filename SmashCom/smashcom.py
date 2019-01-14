#!/usr/bin/python3
"""
author: @brendanmoore42
date: Jan 11, 2019

SmashComm: Control the game.
"""
import time
# from moves import *
import sys

import keyboard
from directkeys import *
import speech_recognition as sr
# from GC_Main import GC_Controller

#instantiate Recognizer class
r = sr.Recognizer()

moves = []
go = sp
version = '1.0.5'

def lets_go():
    """
    Press key to trigger microphone recursively after capture
    """
    print('Press "r" to record.')
    while True:
        try:
            # Record audio
            if keyboard.is_pressed('r'):
                show_me_your_moves()
                break
            # Quit program
            if keyboard.is_pressed('q'):
                return False
        except:
            break
    lets_go()


def show_me_your_moves():
    """
    Opens microphone to take speech then send to controller for function
    """
    with sr.Microphone() as source:
        audio = []
        moves = []
        new_moves = []
        try:
            print("Show me your moves! ")
            #microphone is listening
            audio = r.listen(source, timeout=20, phrase_time_limit=15)
            print('Translating...')
            moves.append(r.recognize_google(audio))
            print(moves)

            # run main fn
            player = GC_Controller(moves=moves)#, move=move, direction=direction, modifier=modifier, mod_move=mod_move, mod_time=mod_time)
            # execute_moves(moves=moves)
        except:
            pass

lets_go()