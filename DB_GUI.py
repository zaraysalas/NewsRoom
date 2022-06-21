# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 20:43:14 2021

@author: salas
"""
from tkinter import *
import DB
import News_GUI
import ctypes
import Prompts

# This windows will collect the parameters to have access to the Workbench
class DB_GUI():
    def __init__(self):
        
        parameters_window = Tk()
        
        parameters_window.title("N E W S   R O O M - Zaray Salas Lopez")
        parameters_window.geometry("+400+150")
        
        params_frame = Canvas(parameters_window, bg = "#006699")
        
        # Run function to get the image
        png_bg = Prompts.Prompts.image_background(400,350, parameters_window, params_frame)
        # Set image as background
        params_frame.create_image(0,0,image = png_bg, anchor = 'nw')
        
        params_frame.pack(expand = YES, fill = BOTH)
        
        intructions_label = Label(params_frame, text = "Parameters to give access to Workbench.", bg = "#006699", font = ('Times New Roman', 0), foreground = "white")
        intructions_label.grid(row = 0, column = 0, columnspan = 2, sticky = 'n', pady = 20, padx = 10)
        
        hostname_label = Label(params_frame, text = "Hostname", bg = "#006699", font = ('Times New Roman', 0), foreground = "white")
        hostname_label.grid(row = 1, column = 0, sticky = 'w', padx = 10)
        hostname = Entry(params_frame, width = 20)
        hostname.grid(row = 1, column = 1, padx = 10)
        
        port_label = Label(params_frame, text = "Port", bg = "#006699", font = ('Times New Roman', 0), foreground = "white")
        port_label.grid(row = 2, column = 0, sticky = 'w', padx = 10)
        port = Entry(params_frame, width = 20)
        port.grid(row = 2, column = 1, padx = 10)
        
        username_label = Label(params_frame, text = "Username", bg = "#006699", font = ('Times New Roman', 0), foreground = "white")
        username_label.grid(row = 3, column = 0, sticky = 'w', padx = 10)
        username = Entry(params_frame, width = 20)
        username.grid(row = 3, column = 1, padx = 10)
        
        password_label = Label(params_frame, text = "Password", bg = "#006699", font = ('Times New Roman', 0), foreground = "white")
        password_label.grid(row = 4, column = 0, sticky = 'w', padx = 10)
        password = Entry(params_frame, show = "*", width = 20)
        password.grid(row = 4, column = 1, padx = 10)
        
        # Pressing this button means that the parameters are saved for future connections to the Workbench Database.
        # With the parameters set, a database is created with a table
        save_button = Button (params_frame, text = "SAVE", command = lambda: DB_GUI.checking_parameters(parameters_window, hostname, port, username, password)
                              , foreground ="#006699", padx = 12, font = ('Times New Roman', 10))
        save_button.grid(row = 5, column = 0, padx = 10, pady = 10)
        # However in the parameters are skip, a popup message is display to alert that the parameters need to be set manually.
        cancel_button = Button (params_frame, text = "CANCEL", command = lambda: [Prompts.Prompts.Close_Window(parameters_window)
                                                                                  , Prompts.Prompts.No_Parameters()
                                                                                  , News_GUI.News_room()]
                                , foreground ="#006699", font = ('Times New Roman', 10))
        cancel_button.grid(row = 5, column = 1, padx = 10, pady = 10)
            
        parameters_window.mainloop()
    
    def checking_parameters(parameters_window, h, po, u, pa):
        hostname = h.get()
        port = po.get()
        username = u.get()
        password = pa.get()
        
        if hostname and port and username and password:
            DB.Saved_News.Parameters(h, po, u, pa)
            Prompts.Prompts.Close_Window(parameters_window)
            DB.Saved_News.Create_DB()
            News_GUI.News_room()
        else:
            Prompts.Prompts.Parameters_Try_Again()
        