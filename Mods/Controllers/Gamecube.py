"""
author: BrendanMoore42
date: Jan 12, 2019

Standard moveset Mod- Gamecube Controller for Dolphin

Games Supported Currently:
Super Smash Bros. Melee
"""
import time
from directkeys import *
# from smash_melee import AddOn

# Add to button list to modify/add phrases
buttons = {'a': ['a'],
           'b': ['b'],
           'x': ['x'],
           'y': ['y'],
           'L': ['L'],
           'R': ['R'],
           'z': ['Z'],
           'up': ['up'],
           'down': ['down'],
           'left': ['left'],
           'right': ['up'],
           'd_up': ['d-pad up'],
           'd_down': ['d-pad down'],
           'd_left': ['d-pad left'],
           'd_right': ['d-pad up'],
           'c_up': ['see up'],
           'c_down': ['see down'],
           'c_left': ['see left'],
           'c_right': ['see up'],
           }

class GC_Controller():
    def __init__(self, moves):
        self.moves = moves
        self.new_moves = moves.split(' ')
        self.direction = direction
        self.modifier = None
        self.mod_move = None
        self.mod_time = None
        self.execute = True
        self.hold = 1

        # int value is where controller looks for number to convert
        # example: hold shield for 4 seconds
        self.modifiers = {'wait', 'hold', 'press', 'side', 'smash', 'tilt', 'tap', 'mash', 'half', 'trigger'}
        self.available_moves = {self.a_press: buttons["a"], self.b_press: buttons["b"],
                                self.down_press: buttons['down'], self.up_press: buttons['up'],
                                self.left_press: buttons['left'], self.right_press: ['right'],
                                self.down_pad_press: buttons['d_down'], self.up_pad_press: buttons['d_up'],
                                self.left_pad_press: buttons['d_left'], self.right_pad_press: ['d_right'],
                                self.down_c_press: buttons['c_down'], self.up_c_press: buttons['c_up'],
                                self.left_c_press: buttons['c_left'], self.right_c_press: ['c_right'],
                                self.hold: buttons['hold']}
        if self.execute:
            #execute move
            [i() for i, x in self.available_moves.items() for move in self.new_moves if move in x]

        def check_modifiers(move, incoming):
            """
            Assign values for modified moves
            :param move: Modifier move to set modifier terms
            :param incoming: Move list coming in from main function
            :return:
            """
            modifier = move

            # get specified number
            try:
                # returns int value from text
                word_index = moves.index(word)
                # get value for modifier to check where number should be
                mod_value = [i for i, x in self.modifiers.items() if word in x]
                # search through the incoming moves to find number to convert
                modifier_index = moves[word_index + mod_value]
                # return the value to modify move
                modifier_out = num_to_int[modifier_index]
            except:
                # defaults to 1 if translation fails
                modifier_out = 1


            return modifier, mod_move, mod_time

        if self.execute:
            for move in self.new_moves:
                if move in self.modifiers:
                    self.modifier, self.mod_move, self.mod_time = check_modifiers(move=move, incoming=self.moves)



                    [i() for i, x in self.available_moves.items() if move in x]


    def execute_moves(self):

        if self.move in self.modifiers:

            [i() for i, x in self.available_moves.items() if self.move in x]



    #Each function is a macro for a specific move
    def wait(self, wait):
        time.sleep(wait)


    def a_press(self, ):

        PressKey(A)
        time.sleep(0.1)
        ReleaseKey(A)


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

    def b_press(self):
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

        def wombo_combo(self, *moves):
            print('sup')

        wombo_combo()

moves = "hey up smash then hold shield for 4 seconds"
move = "smash"
direction = "up" # if not defined will default to last direction called
modifier = "hold"
mod_move = "sheild"
mod_time = 4

player = GC_Controller(moves=moves)