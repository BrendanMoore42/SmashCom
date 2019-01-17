"""
author: BrendanMoore42
date: Jan 12, 2019

Standard button moveset

Can be ported to custom consoles and game-specific packs
"""
import time
from ..DirectKeys.directkeys import *
from .gamecube import GC_Controller


class Controller():
    def __init__(self, moves, execute=True):
        self.moves = moves
        self.new_moves = moves.split(' ')
        self._direction = None
        self._modifier = None
        self._mod_move = None
        self._mod_value = 0

        # Add to button/analog list to modify/add inputs
        self.buttons = {'button': ['a', 'b', 'x', 'y', 'l1', 'l2', 'r1' 'r2', 'z']}

        self.analog = {'analog': ['stick', 'd_pad', 'c_pad']}

        # example: hold shield for 4 seconds
        self.modifiers = {'inputs': ['wait', 'hold', 'press', 'hit', ],
                          'multiplier': ['times'],
                          'pointer': ['side', 'smash', 'tilt',],
                          'direction': ['up', 'down', 'left', 'right'],
                          'other': ['tap', 'mash', 'half', 'degrees'],
                          'action': ['run', 'go', 'walk']}

        # add custom functions here with a list of terms
        self.available_moves = {self.button_press: self.buttons['button'],
                                self.analog_input: self.analog['stick']}

        if self.execute:
            for move in self.new_moves:
                for action, button in self.available_moves.values():
                    if move in button:
                        self._set_modifiers(move=move)
                        if self._modifier:
                            self._execute_moves(move=self.moves, direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time)

            #execute move
            #awesome one liner that won't work --> speech modifiers in the way
            # [i(direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time) for i, x in self.available_moves.items() for move in self.new_moves if move in x]
        else:
            print('First pass next')


    def _set_direction(self, direction):
        self._direction = direction

    def _clear_modifiers(self):
        """Reset modifiers if none present"""
        self._modifier = None
        self._mod_move = None
        self._mod_value = 0


    def _set_modifiers(self, move=None):
        """
        Assign values for modified moves and directions.
        If no mods returns None for variables
        :param move: Modifier move to set modifier terms
        :param incoming: Move list coming in from main function
        :return:
        """
        num_to_int = {'one': 1, 'two': 2, 'three': 3,
                      'four': 4, 'five': 5, 'six': 6,
                      'seven': 7, 'eight': 8, 'nine': 9,
                      'ten': 10, 'half': 0.5}

        if move:
            if move in self.modifiers:
                self._modifier = move
                # get specified number
                try:
                    if move in self.modifiers['inputs']:
                        self._mod_value
                    if move in self.modifiers['pointer']:

                    if move in self.modifiers['direction']:

                    if move in self.modifiers['other']:

                    if move in self.modifiers['action']:



                    # returns int value from text
                    word_index = self.moves.index(move)
                    # get value for modifier to check where number should be
                    mod_value = [i for i, x in self.modifiers.items() if move in x]
                    # search through the incoming moves to find number to convert
                    modifier_index = self.moves[word_index + mod_value]
                    # return the value to modify move
                    modifier_out = num_to_int[modifier_index]
                    self._execute_moves()
                except:
                    self._clear_modifiers()
            else:
                self._clear_modifiers()


    def _execute_moves(self, move):
        pass
        # [i(move, direction) for i, x in self.available_moves.items() if move in x]


    def button_press(self, button, ):
        pass


    def analog_press(self):
        pass


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