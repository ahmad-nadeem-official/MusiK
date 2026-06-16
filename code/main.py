import os
import pygame
import time

def play(path):
    path = path

    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy(): # wait for music to finish playing
        time.sleep(10)

if __name__ == "__main__":    
    path = "/home/muhammad-ahmad-nadeem/Projects/musik/MusiK/code/Kate Bush - Running Up That Hill (Lyrics)  From Stranger Things Season 4 Soundtrack.mp3"

    if not os.path.exists(path):
        print("File not found. Please check the path and try again.")
    else:
        play(path)

    



