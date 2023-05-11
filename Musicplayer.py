#Author Shubham Kumar

import os
import tkinter as tk
import pygame

# set the directory where the music files are located
MUSIC_DIR = "/Users/shubhamkumar/PycharmProjects/musicplayer/Song"

# create a list of music files
music_files = [os.path.join(MUSIC_DIR, file) for file in os.listdir(MUSIC_DIR) if file.endswith(".mp3")]

# initialize pygame
pygame.mixer.init()

# create the main window using tkinter
window = tk.Tk()
window.title("Shubham-🎵Music Player")
window.geometry("600x500")

# create the listbox for displaying the available songs

listbox = tk.Listbox(window, bg='orange', width=35, height=10)

for i, file in enumerate(music_files):
    listbox.insert(i, os.path.basename(file))
listbox.pack()

# create the buttons for controlling the music player
play_button = tk.Button(window, text="Play", command=lambda: pygame.mixer.music.load(
    music_files[listbox.curselection()[0]]) or pygame.mixer.music.play(), bg='green', fg='red')
play_button.pack(side="left")

stop_button = tk.Button(window, text="Stop", command=pygame.mixer.music.stop,fg='blue')
stop_button.pack(side="left")

next_button = tk.Button(window, text="Next",
                        command=lambda: pygame.mixer.music.queue(music_files[listbox.curselection()[0] + 1]))
next_button.pack(side="left")

pause_button = tk.Button(window, text="Pause", command=pygame.mixer.music.pause,fg='blue')
pause_button.pack(side="left")

unpause_button = tk.Button(window, text="Unpause", command=pygame.mixer.music.unpause,fg='red')
unpause_button.pack(side="left")

# create the volume control slider
volume_slider = tk.Scale(window, from_=0, to=10, resolution=1, orient="vertical", label="Volume",
                         command=lambda vol: pygame.mixer.music.set_volume(float(vol)),fg='red')
volume_slider.set(5)
volume_slider.pack()

# main loop for the GUI
window.mainloop()
