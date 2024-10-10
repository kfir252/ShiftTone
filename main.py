from sounds import *
from languages import *
import keyboard


# Listen for ALT+SHIFT key press and handle language change
def keyboard_listener():
    keyboard.add_hotkey('alt+shift', lambda: play_pitch(sound, language_pitch[get_keyboard_language()]))
    keyboard.add_hotkey('caps lock', lambda: play_pitch(sound, (-2, 'SI')))
    keyboard.wait()


if __name__ == "__main__":
    keyboard_listener()
