import ctypes
import keyboard
import pygame
from pydub import AudioSegment
from pydub.playback import play
import io

class Sound:
    # Setup the sound engin
    pygame.mixer.init()
    sound = AudioSegment.from_file("sounds/piano.mp3")

    # Manually (just for now) choosing the note of each language
    pitch = {
        'hebrew': 0,            # Do
        'english': 2/12         # Re
        # 'other': 4/12         # MI
    }


# Returns A new sound object with the modified pitch.
def change_pitch(sound, octaves):
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

# Play the corresponding sound for the detected language
def play_sound_for_language(language):
    if language in pitch:
        modified_sound = change_pitch(sound, pitch[language]).export(io.BytesIO(), format="wav")
        modified_sound.seek(0)
        pygame.mixer.music.load(modified_sound)
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
