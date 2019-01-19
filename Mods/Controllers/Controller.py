"""
author: BrendanMoore42
date: Jan 12, 2019

Standard button moveset

Can be ported to custom consoles and game-specific packs
"""
import re
import time
import itertools as it
from DirectKeys.directkeys import *
from Mods.Controllers.gamecube import GC_Controller


# Approved mods: add here to add quick links to the controller
mods = {'gc': {GC_Controller: {'ssbm': 'Super Smash Bros. Melee', }},
        'nes': {'NES': {'smb': 'Super Mario Bros.'}},
        'pc': {'PC': {'rl': 'Rocket League', }},
        }

class Controller():
    def __init__(self, moves):
        self.moves = moves.lower()
        self.new_moves = moves.split(' ')
        self._direction = None
        self._modifier = None
        self._mod_move = None
        self._mod_value = 0
        self._mod_index = 0
        self.execute = True

        # Add to button/analog list to modify/add inputs
        self.buttons = {'button': ['a', 'b', 'x', 'y', 'l1', 'l2', 'r1' 'r2', 'z']}
        self.analog = {'analog': ['stick', 'dpad', 'cstick']}

        # Add macros and custom functions here
        self.mod_phrases = {'dpad': ['d-pad', 'd pad'],
                            'cstick': ['c stick', 'c-stick', 'see stick', 'cystic']}

        # example: hold shield for 4 seconds
        self.modifiers = {'inputs': ['wait', 'hold', 'press', 'hit', ],
                          'multiplier': ['times', 'once', 'twice', 'thrice'],
                          'pointer': ['side', 'smash', 'tilt', 'flick'],
                          'direction': ['up', 'down', 'left', 'right'],
                          'other': ['tap', 'mash', 'half', 'degrees', 'seconds'],
                          'action': ['run', 'go', 'walk'],
                          'buttons': self.buttons['button'],
                          'analog': self.analog['analog']}

        # add custom functions here with a list of terms
        self.available_moves = {self.button_press: self.buttons['button'],
                                self.analog_input: self.analog['analog'],
                                self._set_modifiers: list(it.chain.from_iterable(self.modifiers.values()))}

        # debug for stopping during tests
        if self.execute:
            print(self.new_moves)

            #search for phrases first --> replace phrase in moves for transport to new_moves
            self._replace_phrases(moves)

            # look for modifiers first
            for move in self.new_moves:
                try:
                    if move in list(it.chain.from_iterable(self.modifiers.values())):
                        print(move + '!')
                        self._set_modifiers(move=move)

                    # for action, button in self.available_moves.items():
                    #     # move will execute the function, or branch further if modifier present
                    #     if move in button:
                    #         action()
                    #         self._set_modifiers(move=move)
                            # if self._modifier:
                            #     self._execute_moves(move=self.moves, direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time)
                # iterate through each move and look for match in controller/modifier dictionaries
                except:
                    print('not a modifier')
            #execute move
            #awesome one liner that won't work --> speech modifiers in the way
            # [i(direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time) for i, x in self.available_moves.items() for move in self.new_moves if move in x]
        else:
            print('First pass next')


    def _replace_phrases(self, moves):
        """
        Takes the moves list and replaces phrases with key pair for move execution
        :param moves:
        """

        def _generate_ngrams(moves, n):
            """Generates list of ngrams from moves with n value"""
            # Convert to lowercases
            moves = moves.lower()

            # Replace all none alphanumeric characters with spaces
            moves = re.sub(r'[^a-zA-Z0-9\s]', ' ', moves)

            # Break sentence in the token, remove empty tokens
            tokens = [token for token in moves.split(" ") if token != ""]

            # Use the zip function to help us generate n-grams
            # Concatentate the tokens into ngrams and return
            ngrams = zip(*[tokens[i:] for i in range(n)])
            return [" ".join(ngram) for ngram in ngrams]



        bigram_list = _generate_ngrams(moves, 2)

        for phrase in bigram_list:
            for mod, mod_list in self.mod_phrases.items():
                if phrase in mod_list:
                    print(phrase + '!!')


        self.moves = modified_moves


    def _set_direction(self, direction):
        self._direction = direction


    def _clear_modifiers(self):
        """Reset modifiers if none present"""
        self._modifier = None
        self._mod_move = None
        self._mod_value = 0


    def _set_modifiers(self, move):
        """
        Assign values for modified moves and directions.
        If no mods returns None for variables
        :param move: Modifier move to set modifier terms
        :param incoming: Move list coming in from main function
        :return:
        """

        # set modifier for parsing
        self._modifier = move

        # get specified number
        def _fetch_values(mod_type):
            """
            Find the number in the phrase and generate a int value. Mod type will search
            for numbers in different spaces.
            """
            num_to_int = {['one', 'once']: 1, ['two', 'twice']: 2, ['three', 'thrice']: 3,
                          'four': 4, 'five': 5, 'six': 6,
                          'seven': 7, 'eight': 8, 'nine': 9,
                          'ten': 10, 'half': 0.5}

            if mod_type == 'inputs':
                try:
                    # returns int value from text
                    word_index = self.moves.index(self._modifier)
                    # get value for modifier to check where number should be
                    mod_value = [i for i, x in self.modifiers.items() if move in x]
                    # search through the incoming moves to find number to convert
                    modifier_index = self.moves[word_index + mod_value]
                    # return the value to modify move
                    modifier_out = num_to_int[modifier_index]
                except:
                    print('nope')

        try:
            if self._modifier in self.modifiers['inputs']:
                _fetch_values('input')
                pass
            if self._modifier in self.modifiers['pointer']:
                pass
            if self._modifier in self.modifiers['direction']:
                pass
            if self._modifier in self.modifiers['other']:
                pass
            if self._modifier in self.modifiers['action']:
                pass
        except:
            self._clear_modifiers()



    def _execute_moves(self, move):
        pass
        # [i(move, direction) for i, x in self.available_moves.items() if move in x]


    def button_press(self, button, ):
        pass


    def analog_input(self):
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


moves = "press stick left for ten seconds then d-pad up twice and flick c stick down"
moves1 = "run right and press a button three times"
move = "stick"
direction = "left" # if not defined will default to last direction called
modifier = "press"
mod_move = "shield"
mod_time = 10

player = Controller(moves=moves)