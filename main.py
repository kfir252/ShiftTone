from sounds_manager import *
from languages_manager import *
from keys_manager import *
import keyboard


# Listen for ALT+SHIFT key press and handle language change
def keyboard_listener():
    for hotkey, func in hotkeys_functions.items():
        keyboard.add_hotkey(hotkey, func)
    keyboard.wait()


if __name__ == "__main__":
    keyboard_listener()
