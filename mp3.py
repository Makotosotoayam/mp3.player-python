from tkinter import filedialog
from tkinter import *
import pygame
import os

win = Tk()
win.title('MP3 Player')
text= Label(win, text="MP3 PLAYER\nHello nice to see you again",font=('Gotham Rounded Medium', 20,))
#you need to install the font into your computer in order this code above can work

text.pack(pady=30)
win.geometry("250x150")

win.attributes('-fullscreen',True)

pygame.mixer.init()

menubar = Menu(win)
win.config(menu=menubar)

songs = []
current_song = ""
paused = False

def loadmusic():
    global current_song
    win.directory = filedialog.askdirectory()

    for song in os.listdir(win.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert('end', song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def playmusic():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(win.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pausemusic():
    global paused
    pygame.mixer.music.pause()
    paused = True

def nextmusic():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        playmusic()
    except:
        pass

def prevmusic():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song = songs[songlist.curselection()[0]]
        playmusic()
    except:
        pass

def set_volume(val):
    pygame.mixer.music.set_volume(float(val)/100)

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select folder', command=loadmusic)
menubar.add_cascade(label='Organise', menu=organise_menu)

win.attributes('-fullscreen', False)

volume_frame = Frame(win)
volume_frame.pack(pady=5)
volume_label = Label(volume_frame, text="Volume", font=('Gotham Rounded Medium', 14))
volume_label.pack(side=LEFT)
volume_slider = Scale(volume_frame, from_=0, to=100, orient=HORIZONTAL, command=set_volume, length=250)
volume_slider.set(50)  # Set default volume to 50%
volume_slider.pack(side=TOP)

songlist = Listbox(win, bg='#1DB954', fg='white', width=220, height=27)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
prev_btn_image = PhotoImage(file='previous.png')

control_frame = Frame(win)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0,command=playmusic)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0,command=pausemusic)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0,command=nextmusic)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0,command=prevmusic)

play_btn.grid(row=0, column=2, padx=7, pady=10)
pause_btn.grid(row=0, column=3, padx=7, pady=10)
next_btn.grid(row=0, column=1, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)



win.mainloop()

