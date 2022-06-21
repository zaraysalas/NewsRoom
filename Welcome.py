# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:00:17 2021
@author: zaray salas lopez
"""
from tkinter import *
import time
import News_GUI
import DB_GUI
import Prompts
import os
from PIL import Image, ImageTk


# ----------Welcome window to the news room--------------
class Welcome():
    def __init__(self):
        welcome_window = Tk()
        welcome_window.geometry("+400+150")
        welcome_window.title("N E W S   R O O M")
                
        # Blue as color design
        welcome_frame = Canvas(welcome_window, bg = "#006699")
                
        # Run function to get the image
        png_bg = Prompts.Prompts.image_background(700, 600, welcome_window, welcome_frame)
        # Set image as background
        welcome_frame.create_image(0,0,image = png_bg, anchor = 'nw')
        welcome_frame.pack(expand = YES, fill = BOTH)
        
        
        # Font and color design for the labels with different font size.
        label_welcome = Label(welcome_frame, text = "W E L C O M E  T O", bg = "#006699", font = ('Times New Roman', 30), foreground = "white").pack()

        label_news = Label(welcome_frame, text = "N E W S   R O O M", bg = "#006699", font = ('Times New Roman', 60), foreground = "white" ).pack(padx = 15)
        
        # Label with today's day, month, day number and year.
        label_date = Label(welcome_frame, text = time.strftime("%A, %B %d %Y"), bg = "#006699", font = ('Times New Roman', 30), foreground = "white").pack()
        # Label with current time in 24 hrs format.
        label_time = Label(welcome_frame, text = time.strftime("%X"), bg = "#006699", font = ('Times New Roman', 30), foreground = "white").pack()
        # Label with Student's name
        label_student = Label(welcome_frame, text = "by ZARAY SALAS LOPEZ", bg = "#006699", font = ('Times New Roman', 15), foreground = "white").pack(pady = 40)
        # Button to go to the second window with the news.
        go_news_room = Button (welcome_frame, text = "GO TO NEWS ROOM", command = lambda: [Prompts.Prompts.Close_Window(welcome_window)
                                                                                           , DB_GUI.DB_GUI()]
                               , foreground ="#006699", padx = 10, pady = 10, font = ('Times New Roman', 13, 'bold'))
        go_news_room.pack(pady = 30)
        
        
        welcome_window.mainloop()
        
Welcome()