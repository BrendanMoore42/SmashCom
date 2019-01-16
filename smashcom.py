#!/usr/bin/python3
"""
author: @brendanmoore42
date: Jan 11, 2019

SmashComm: Control the game.
"""
import sys
import time
import keyboard
import speech_recognition as sr
# from Mods.Controllers import Controller, Gamecube
# from Mods.Controllers.DirectKeys.directkeys import *

#instantiate Recognizer class
r = sr.Recognizer()
version = '1.0.6'

# Approved mods, add here to add quick links to the controller
# mods = {'gc': {Gamecube: {'ssbm': 'Super Smash Bros. Melee', }},
#         'nes': {'NES': {'smb': 'Super Mario Bros.'}},
#         'pc': {'PC': {'rl': 'Rocket League', }},
#         }

class SmashCom():
    """
    To run SmashCom: create new SmashCom instance, be sure to specify mods or games if any, or defaults to
    standard controller.
    """

    def __init__(self, controller, game):
        self.controller = controller
        self.game = game


    def lets_go(self):
        """
        Press key to trigger microphone recursively after capture
        """
        print('Press "r" to record.')
        while True:
            try:
                # Record audio
                if keyboard.is_pressed('r'):
                    self.show_me_your_moves(self.controller, self.game)
                    break
                # Quit program
                if keyboard.is_pressed('q'):
                    return False
            except:
                break
        self.lets_go()


    def show_me_your_moves(self, controller, game):
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
               # player = Controller(moves=moves, execute=False)#, move=move, direction=direction, modifier=modifier, mod_move=mod_move, mod_time=mod_time)
                # execute_moves(moves=moves)
            except:
                pass


# For Testing
# main function
def main(args):
    """
    args[1] = Controller
    args[2] = Game

    python smashcom.py gamecube melee
    """

    # create file names to use in functions
    controller = args[1]
    game = args[2]

    if controller.lower() in mods.keys():
        print(controller)
    print(controller, game)

    #debug_init = SmashCom(controller=controller, game=game)

if __name__ == '__main__':
    # temp_args = ['smashcom.py', 'gc', 'ssbm']
    # main(temp_args)
    sc = SmashCom()
    sc.lets_go()