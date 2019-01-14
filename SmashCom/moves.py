"""
author: @brendanmoore42
date: Jan 11, 2019

SmashComm: Control the game.

Moves

Main function to parse instructions and execute moves
"""

import sys
import time
from directkeys import *

moves_list = ['','']
# dash = 1
# hold = dash * time

#modifiers that influence timings
modifiers = {1: ["up", "down", "left", "right"],
             2: ["double", "once", "twice",],
             3: ["hold", "wait", "triple"],
             4: ["quadruple", "four"]}

num_to_int = {'one': 1, 'two': 2, 'three': 3,
              'four': 4, 'five': 5, 'six': 6,
              'seven': 7, 'eight': 8, 'nine': 9,
              'ten': 10, 'half': 0.5}

#available moves
# moves_list = {single: {'jab':jab(), 'crouch':crouch(), 'shield':shield(), 'grab':grab(), 'wd':wd(),},
#               double: {'jump':jump(), 'djab': djab(),},
#               quat: {'up', 'down', 'left', 'right',},
#               quin: {'lsmash', 'laser', 'shdl', 'wd', }}

def quit_game(moves):
    exit_phrases = ["melee should have tripping", 'brawl was better', 'luigi is a gimmick', 'quit game']
    if moves in exit_phrases:
        print('No Johns')
        sys.exit()

def check_modifier(word, modifiers):

    def get_value(word, moves):
        """

        :param word: Incoming modifier
        :param moves: Incoming instructions from speech
        :param index: Where to search for number modifier
        :return:
        """
        try:
            # returns int value from text
            word_index = moves.index(word)
            # get value for modifier to check where number should be
            mod_value = [i for i,x in modifiers.items() if word in x]
            # search through the incoming moves to find number to convert
            modifier_index = moves[word_index + mod_value]
            # return the value to modify move
            modifier_out = num_to_int[modifier_index]
        except:
            # defaults to 1 if translation fails
            modifier_out = 1
        return modifier_out

    if word in modifiers:
        if word == 'hold':
            modifier = get_value(word)
    print('***')
    print(modifier)

    return modifier


def execute_moves(moves):

    # check if quit phrase activated
    quit_game(moves)
    # print what the recognizer hears
    print(moves)
    # splits the moves and checks for associations
    new_moves = [words for segments in moves for words in segments.split()]

    # iterate through each move
    for word in new_moves:
        #check if move is a modifier -> new tree
        action, modifier = check_modifier(word, modifiers)
        if modifier:
            print('yay')
            break




    try:
            if action == 'hold':
                pass
            if action in moves_list:
                moves_list[action]


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
            elif action == "wave":
                wd_left()
            else:
                pass
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


class Move():

    def __init__(self):
        self.hold = 3
        self.wait = 3
        self.tilt = 'left'
        self.smash = 'right'

    #Each function is a macro for a specific move
    def wait(self, wait):
        time.sleep(wait)


    def jump(self):
        PressKey(T)
        time.sleep(0.1)
        ReleaseKey(T)


    def up(self):
        PressKey(UP)
        time.sleep(0.25)
        ReleaseKey(UP)


    def left(self):
        PressKey(LEFT)
        time.sleep(0.1)#To alter timing of presses
        ReleaseKey(LEFT)


    def right(self):
        PressKey(RIGHT)
        time.sleep(0.1)
        ReleaseKey(RIGHT)


    def crouch(self):
        PressKey(DOWN)
        time.sleep(0.1)
        ReleaseKey(DOWN)


    def jab(self):
        PressKey(A)
        time.sleep(0.05)
        ReleaseKey(A)


    def djab(self):
        PressKey(A)
        ReleaseKey(A)
        time.sleep(0.05)
        PressKey(A)
        ReleaseKey(A)


    def shield(self):
        PressKey(R)
        time.sleep(2)
        ReleaseKey(R)


    def grab(self):
        PressKey(Z)
        time.sleep(0.05)
        ReleaseKey(Z)


    def Rsmash(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def Lsmash(self):
        PressKey(LEFT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(LEFT)
        ReleaseKey(A)

    def laser(self):
        PressKey(B)
        time.sleep(0.05)
        ReleaseKey(B)

    def shdl(self):
        PressKey(Y)
        PressKey(B)
        ReleaseKey(B)
        PressKey(B)
        ReleaseKey(B)


    def shine(self):
        PressKey(DOWN)
        PressKey(B)
        time.sleep(0.05)
        ReleaseKey(DOWN)
        ReleaseKey(B)


    def wd_left(self):
        PressKey(X)
        time.sleep(0.05)
        PressKey(DOWN), PressKey(LEFT)
        PressKey(R)
        ReleaseKey(R), ReleaseKey(DOWN), ReleaseKey(LEFT)


    def wd_right(self):
        PressKey(X)
        time.sleep(0.05)
        PressKey(DOWN), PressKey(RIGHT)
        PressKey(R)
        ReleaseKey(R), ReleaseKey(DOWN), ReleaseKey(RIGHT)

player = Move()
player.jab()