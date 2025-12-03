# import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# keyboard main instance 
keyboard = KMKKeyboard()

# macro extension
macros = Macros()
keyboard.modules.append(macros)

# 4 pins (switches) on the board
PINS = [board.D4, board.D3, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MACRO("Hi there! key1: help \n key2: <ALT><tab> \n key3 <CTL><tab> \n key4: <WIN><tab>"), 
     KC.Macro(Press(KC.LALT), Delay(10), Tap(KC.TAB), Delay(10), Release(KC.LALT)),
     KC.Macro(Press(KC.LCTL), Delay(10), Tap(KC.TAB), Delay(10), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCMD), Delay(10), Tap(KC.TAB), Delay(10), Release(KC.LCMD)),
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
