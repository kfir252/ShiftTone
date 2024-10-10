from sounds_manager import *
from languages_manager import *

hotkeys_functions = {
    'alt+shift': lambda: play_pitch(*language_sound[get_keyboard_language()]),
    'caps lock': lambda: play_pitch(sounds['fart'], -2, 'SI')
}