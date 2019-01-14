# SmashCom 
SmashCom is a custom vocal controller that takes user speech and converts the instructions to pre-set button inputs. Inspired by Super Smash Bros. and games with a deep lexicon, SmashCom can correctly interpret and use modifiers in colloquialisms to string more complex actions together. 

### Mods
SmashCom is currently designed and actionable for the Nintendo Gamecube, however, can be modified to work with any emulator by development of AddOn controller packs located in the Mods folder. If you want to try creating a NES, SNES, Playstation Dualshock or other controller scheme, or add game-specific language packs, please clone the repository and if it works we'll add it to the project. 

### Example: Smash Bros. Melee
The Smash Bros community has developed a wide list of unique (and borrowed from other fighters) move names that are used to describe gameplay. Terms like waveshine, flutterhush, or thunders describe both moves and combos - a series of buttons to be pressed in a particular order and timing. 

SmashCom will pick out words and then initaite moves/combos that it hears in your instructions, in the order it hears them. For example, "Fox, run right, multishine and jump", will play the sequence: run right, press down-B rapidly to shine three times, X to jump. It will only pay attention to the smash bros. specific instructions. SmashCom will apply modifiers like "hold", "wait', or "mash" with the specified number of seconds or button presses to create a whole different kind of dynamic gaming experience.  

## Setup

Tested on Windows 10. Requires Python 3.6+. 
Requirements incoming. 

### Running Melee on Dolphin
1. Any version of Dolphin GC emulator: https://dolphin-emu.org/. Or Netplay build: https://www.smashladder.com/guides/view/272o/play-melee-online-netplay-guide-faster-melee-5-8-7-with-uc
2. Acquire Melee v1.02 NTSC. Load into Dolphin.
3. Configure Dolphin controller:  
  a) Select controllers.  
  b) Port 1 select "Standard Controller", configure.  
  c) Device == DInput/0/Keyboard Mouse.  
  d) Map buttons relating to directkeys.py or custom mapping (if creating custom maps).  
4. Open Melee, navigate to desired mode, Training mode to test recommended.

### Initialize
In terminal run: 

    $ python3 smashcom.py

Wait for 'Show me your moves...' to print before saying your command. It's using Google's Speech Recognition API, so translation can sometime be inaccurate and take a few seconds. Smash commander really shines when two people play over netplay each using vocal commands. 
