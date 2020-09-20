import tkinter as tkr
import os
import pygame
from tkinter import ttk

var = None

class Music_player:
    def __init__(self,master):
        master.title("Music Player")
        frame = tkr.LabelFrame(master, text = "controls" , bd = 3)
        frame.grid(row = 1, column=0)
        frame2 = tkr.LabelFrame(master, text = "Songlist", bd = 3)
        frame2.grid(row = 1, column = 1)
        frame3 = tkr.LabelFrame(master, text = "Sound Controls", bd = 3)
        frame3.grid(row = 1, column = 2)
        frame4 = tkr.LabelFrame(master, text = "Now Playing", bd = 3)
        frame4.grid(row = 0, column = 1)

        pygame.mixer.init()

        self.btn = ttk.Button(frame,text="PLAY", style="C.TButton", command=self.play)
        self.btn.grid(ipadx=15,ipady=5)
        self.btn1 = ttk.Button(frame,text="STOP", style="C.TButton", command=self.stop)
        self.btn1.grid(ipadx=15,ipady=5)
        self.btn2 = ttk.Button(frame, text = "PAUSE", style="C.TButton", command = self.pause)
        self.btn2.grid(ipadx=15,ipady=5)
        self.btn3 = ttk.Button(frame, text = "UNPAUSE", style="C.TButton", command = self.unpause)
        self.btn3.grid(ipadx=15,ipady=5)
        self.btn4 = ttk.Button(frame3, text = "MUTE", style="C.TButton", command = self.mute)
        self.btn4.grid(ipadx=15,ipady=5)
        self.btn5 = ttk.Button(frame3, text = "UNMUTE", style="C.TButton", command = self.unmute)
        self.btn5.grid(ipadx=15,ipady=5)

        
        self.volumeslider = tkr.Scale(frame3, from_=0.0,to=1, resolution = 0.1, showvalue='yes',
             cursor ="arrow", orient = tkr.HORIZONTAL, activebackground = "#A358A3", trough = '#D472D4', command = self.change_volume)
        self.volumeslider.grid()
        
        os.chdir("C:/Users/prath/Music")
        songlist = os.listdir()


        self.playlist = tkr.Listbox(frame2, highlightcolor = "purple", selectbackground = "purple", font= ("Monlo-Regular",10), width = 60,
         selectmode=tkr.SINGLE)
        self.playlist.grid()
        for items in songlist:
            if items.endswith(".mp3"):
                self.playlist.insert(0, items)
                

        style = ttk.Style()
        style.configure('TButton', foreground="black", highlightthickness=5,
                        highlightbackground='purple', highlightforeground="white",
                        activebackground="black")

        style.map("C.TButton",
            foreground=[('pressed', 'red'), ('active', 'purple')],
            background=[('pressed', '!disabled', 'black'), ('active', 'black')]
            )


        
        global var
        var = tkr.StringVar()
        self.songtitle = tkr.Label(frame4, textvariable = var, width = 50)
        self.songtitle.grid()

        


    def play(self):
        pygame.mixer.music.load(self.playlist.get(tkr.ACTIVE))
        var.set(self.playlist.get(tkr.ACTIVE))
        pygame.mixer.music.set_volume(self.volumeslider.get())
        pygame.mixer.music.play()
        
    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.set_volume(self.volumeslider.get())
        pygame.mixer.music.unpause()

    def mute(self):
        pygame.mixer.music.set_volume(0)

    def unmute(self):
        pygame.mixer.music.set_volume(self.volumeslider.get())

    def change_volume(self,_=None):
        pygame.mixer.music.set_volume(self.volumeslider.get())

root = tkr.Tk()
a = Music_player(root)
root.mainloop()
