import pygame as pg
import os

pg.init()

width = 400
height = 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Music-player')

music_dir = "./music/"
music_files = os.listdir(music_dir)
current_music = 0
pg.mixer.music.load(music_dir + music_files[current_music])
"""
music_sound = [
    pg.mixer.Sound('music/essence.mp3'),
    pg.mixer.Sound('music/tinashe.mp3'),
    pg.mixer.Sound('music/konfuci.mp3')
]
"""
key_play = pg.K_SPACE
key_next = pg.K_RIGHT
key_prev = pg.K_LEFT

pg.mixer.music.play()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == key_play:
                if pg.mixer.music.get_busy(): #function
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()

            elif event.key == key_next:
                current_music = (current_music + 1) % len(music_files)
                pg.mixer.music.load(music_dir + music_files[current_music])
                pg.mixer.music.play()

            elif event.key == key_prev:
                current_music = (current_music - 1) % len(music_files)
                pg.mixer.music.load(music_dir + music_files[current_music])
                pg.mixer.music.play()
pg.quit()