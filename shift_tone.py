from helper import *

# Setup the sound engin and
pygame.mixer.init()
sound = AudioSegment.from_file("C:\ShiftTone\sounds\piano.mp3")

# Detect the current keyboard language
def get_keyboard_language():
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    threadID = user32.GetWindowThreadProcessId(hwnd, None)
    klid = user32.GetKeyboardLayout(threadID)
    lang_id = klid & (2**16 - 1)

    if lang_id == 1033:  
        return 'hebrew'
    elif lang_id == 1037:  
        return 'english'
    else:
        return 'unknown'


    
# Listen for ALT+SHIFT key press and handle language change
def listen_for_shift_alt():
    keyboard.add_hotkey('alt+shift', lambda: play_pitch(sound, language_pitch[get_keyboard_language()]))
    keyboard.add_hotkey('caps lock', lambda: play_pitch(sound, (1, 'MI')))
    keyboard.wait()


if __name__ == "__main__":
    listen_for_shift_alt()
