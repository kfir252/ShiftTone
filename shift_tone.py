import ctypes
import keyboard
import pygame

# Sound files
sounds = {
    'hebrew': 'sounds/hebrew.mp3',
    'english': 'sounds/english.mp3'
}

# Play the corresponding sound for the detected language
def play_sound_for_language(language):
    pygame.mixer.init()
    if language in sounds:
        pygame.mixer.music.load(sounds[language])
        pygame.mixer.music.play()

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
    keyboard.add_hotkey('alt+shift', lambda: play_sound_for_language(get_keyboard_language()))
    keyboard.wait()

if __name__ == "__main__":
    listen_for_shift_alt()


