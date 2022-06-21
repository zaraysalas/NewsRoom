# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 04:09:21 2021

@author: salas
"""
import ctypes
import os
from tkinter import *
from PIL import Image, ImageTk

class Prompts():
    def Close_Window(window):
        # Close the Welcome window
        window.destroy()
    
        # PopUp messages
        
    def No_Parameters():
        ctypes.windll.user32.MessageBoxW(0, "As the parameters are not set now. \n They must be set manually at DB.Saved_News.Connect", "ALERT", 64)
        
    def No_Number():
        ctypes.windll.user32.MessageBoxW(0, "'Month' needs to be a number between \n greater than 01 and 12 \n\n 'Day' needs to be a number between \n greater than 01 and 31 ", "TRY AGAIN", 64)
    
    def Parameters_Try_Again():
        ctypes.windll.user32.MessageBoxW(0, "Four parameters are mandatory \n If parameters does not want to be save press CANCEL", "TRY AGAIN", 64)
      
    def image_background(w, h, root, canvas):
        # All widgets with color "#006699" become transparent
        #root.wm_attributes('-transparentcolor', "#006699")
        # Get the image
        im = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "news_background.jpg"))
        # Reduce the size of the image
        im.thumbnail((w, h))
        png_bg = ImageTk.PhotoImage(im, master = root)
        
        return png_bg