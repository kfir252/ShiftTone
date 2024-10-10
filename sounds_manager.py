import pygame
pygame.mixer.init()

from pydub import AudioSegment
from pydub.playback import play
import io


# Mapping note to it's HZ
note_HZ = {
    'DO'    : 0,
    'RE'    : 2/12,
    'MI'    : 4/12,
    'FA'    : 5/12,
    'SOL'   : 7/12,
    'LA'    : 9/12,
    'SI'    : 11/12
}

sounds = {
    'piano': "piano.mp3",
    'fart': "Fart.mp3",
    'duck': "Duck Quack.mp3"
}

for name, filename  in sounds.items():
    sounds[name] = AudioSegment.from_file("C:\ShiftTone\sounds\\" + filename)
   

# Returns A new sound object with the modified note.
def change_pitch(sound, octaves, note):
    new_sample_rate = int(sound.frame_rate  * (2.0 ** (octaves + note_HZ[note])))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

def play_sound(sound):
    modified_sound = sound.export(io.BytesIO(), format="wav") 
    modified_sound.seek(0)
    pygame.mixer.music.load(modified_sound)
    pygame.mixer.music.play()
    
def play_pitch(sound, octaves, note):
    play_sound(change_pitch(sound, octaves, note))