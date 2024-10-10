import ctypes


# Manually choosing the note of each language
language_pitch = {
    'hebrew': (0, 'DO'),
    'english': (1, 'RE')
}

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