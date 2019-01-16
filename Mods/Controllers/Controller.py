"""
author: BrendanMoore42
date: Jan 12, 2019

Standard button moveset

Can be ported to custom consoles and game-specific packs
"""
import time
from .DirectKeys.directkeys import *

# Add to button list to modify/add phrases
# key : list of strings to interpret
buttons = {'a': ['a'],
           'b': ['b'],
           'x': ['x'],
           'y': ['y'],
           'L': ['l'],
           'R': ['r'],
           'z': ['z'],
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

class Controller():
    def __init__(self, moves, execute=True):
        self.moves = moves
        self.new_moves = moves.split(' ')
        self._direction = None
        self._modifier = None
        self._mod_move = None
        self._mod_time = None

        # int value is where controller looks for number to convert
        # example: hold shield for 4 seconds
        self.modifiers = {'inputs': ['wait', 'hold', 'press',],
                          'pointer': ['side', 'smash', 'tilt',],
                          'direction': ['up', 'down', 'left', 'right'],
                          'other': ['tap', 'mash', 'half',],
                          'action': ['run', 'go',]}

        # add custom functions here with a list of terms
        self.available_moves = {self.a_press: buttons["a"], self.b_press: buttons["b"],
                                self.down_press: buttons['down'], self.up_press: buttons['up'],
                                self.left_press: buttons['left'], self.right_press: ['right'],
                                self.down_pad_press: buttons['d_down'], self.up_pad_press: buttons['d_up'],
                                self.left_pad_press: buttons['d_left'], self.right_pad_press: ['d_right'],
                                self.down_c_press: buttons['c_down'], self.up_c_press: buttons['c_up'],
                                self.left_c_press: buttons['c_left'], self.right_c_press: ['c_right']}
        if self.execute:
            for move in self.new_moves:
                for action, word in self.available_moves.values():
                    if move in word:
                        self._set_modifiers(move=move)
                        self._execute_moves(move=self.moves, direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time)

            #execute move
            #awesome one linrer that won't work
            # [i(direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time) for i, x in self.available_moves.items() for move in self.new_moves if move in x]
        else:
            print('First pass next')


        def _set_modifiers(move=None):
            """
            Assign values for modified moves and directions
            :param move: Modifier move to set modifier terms
            :param incoming: Move list coming in from main function
            :return:
            """
            if move:
                if move in self.modifiers:
                    self._modifier = move
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
                        # set default values if
                        self._modifier = None
                        self._mod_move = None
                        self._mod_time = None

        #
        # if self.execute:
        #     for move in self.new_moves:
        #         if move in self.modifiers:
        #             self.modifier, self.mod_move, self.mod_time = check_modifiers(move=move, incoming=self.moves)
        #
        #
        #
        #             [i() for i, x in self.available_moves.items() if move in x]


    def _execute_moves(self, move, direction, modifier=False):

        if modifier:

        if self.move in self.modifiers:

            [i() for i, x in self.available_moves.items() if self.move in x]


    def a_press(self, ):

        PressKey(A)
        time.sleep(0.1)
        ReleaseKey(A)


    def b_press(self, ):

        PressKey(A)
        time.sleep(0.1)
        ReleaseKey(A)


    def r_press(self):
        PressKey(R)
        time.sleep(2)
        ReleaseKey(R)


    def l_press(self):
        PressKey(L)
        time.sleep(2)
        ReleaseKey(L)


    def z_press(self):
        PressKey(Z)
        time.sleep(0.05)
        ReleaseKey(Z)


    def up(self):
        PressKey(UP)
        time.sleep(0.25)
        ReleaseKey(UP)


    def left(self):
        PressKey(LEFT)
        time.sleep(0.1)#To alter timing of presses self.modifier
        ReleaseKey(LEFT)


    def right(self):
        PressKey(RIGHT)
        time.sleep(0.1)
        ReleaseKey(RIGHT)


    def down(self):
        PressKey(DOWN)
        time.sleep(0.1)
        ReleaseKey(DOWN)


    def up_pad_press(self):
        PressKey(A)
        time.sleep(0.05)
        ReleaseKey(A)


    def down_pad_press(self):
        PressKey(A)
        ReleaseKey(A)
        time.sleep(0.05)
        PressKey(A)
        ReleaseKey(A)


    def c_up_press(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def c_down_press(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def c_left_press(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def c_right_press(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)




#
# moves = "hey up smash then hold shield for 4 seconds"
# move = "smash"
# direction = "up" # if not defined will default to last direction called
# modifier = "hold"
# mod_move = "sheild"
# mod_time = 4
#
# player = StdController(moves=moves)