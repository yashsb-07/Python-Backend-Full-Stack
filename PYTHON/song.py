import sys
import time
import pygame

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("D:\My-Projects\Python Full-Stack\PYTHON\Finding Her.mp3")  
    pygame.mixer.music.play()

def print_lyrics():
    lyrics = [
        "Sambhaal ke rakha wo phool mera tu",
        "Meri shayari mein zaroor raha tu",
        "Jo aankhon mein pyaari si duniya basaayi",
        "Wo duniya bhi tha tu, wo lamha bhi tha tu",
        "Haan, lagte hain mujhko ye kisse sataane",
        "Deta na dil mera tujhko bhulaane",
        "Adhoore se vaade, adhoori si raatein",
        "Ab hisse mein daakhil mere bas wo yaadein"
    ]

    delays = [0.7, 0.7, 0.4, 0.5, 0.5, 0.7, 0.7, 1.0]

    print("Finding Her..🥺💗 \n")
    time.sleep(1.2)

    for i, line in  enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delays[i])
    
play_song()
print_lyrics()

while pygame.mixer.music.get_busy():
    time.sleep(1)