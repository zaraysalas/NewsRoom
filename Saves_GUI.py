# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 03:33:24 2021

@author: salas
"""

from tkinter import *
import DB
import News_GUI
import Prompts
import webbrowser

class Saved_List():
    def __init__(self, news_room_window):
        self.news_room_window =news_room_window
        saves = Tk()
        
        news_list = DB.Saved_News.Retrive_saved_news(news_room_window,saves)
        
        saves.title("Y O U R   N E W S   S A V E D - Zaray Salas Lopez")
        saves.geometry("1315x400+50+50")
        
        head_frame = Canvas(saves, bg = "indian red")
        head_frame.pack(expand = FALSE, fill = BOTH)
        
        # Press the button to go back for more news.
        back_to_news = Button(head_frame, text = "GO BACK FOR MORE NEWS", command = lambda: [Prompts.Prompts.Close_Window(saves)
                                                                              , News_GUI.News_room()]
                              , bg = "indian red", font = ('Times New Roman', 13))
        back_to_news.pack(pady = 25)
        
        # Set the left scrollbar.
        wraper = LabelFrame(saves)
        
        canvas = Canvas(wraper, bg = "indian red")
        canvas.pack(side = LEFT, fill = 'both', expand = 'yes')
        
        scrollbar = Scrollbar(wraper, orient = 'vertical', command = canvas.yview)
        scrollbar.pack(side = RIGHT, fill = 'y')
        
        
        canvas.configure(yscrollcommand = scrollbar.set)
        
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))
        
        frame = Canvas(canvas, bg = "indian red")
        canvas.create_window((0,0), window = frame, anchor = 'nw')
        
        wraper.pack(fill = 'both', expand = 'yes')
                
        # Labels for the columns
        id_news = Label(frame, text = "ID", bg = "indian red", font = ('Times New Roman', 0)).grid(row = 0, column = 0, pady = 15)
        news_date = Label(frame, text = "DATE", bg = "indian red", font = ('Times New Roman', 0)).grid(row = 0, column = 1)
        news_brief = Label(frame, text = "BRIEF", bg = "indian red", font = ('Times New Roman', 0)).grid(row = 0, column = 2)
        news_website = Label(frame, text = "WEBSITE", bg = "indian red", font = ('Times New Roman', 0)).grid(row = 0, column = 3)
        news_section = Label(frame, text = "SECTION", bg = "indian red", font = ('Times New Roman', 0)).grid(row = 0, column = 4)
        news_country = Label(frame, text = "COUNTRY", bg = "indian red", font = ('Times New Roman', 0)).grid(row = 0, column = 5)
        
        # Takes the data from the List and distribute it in the window.
        # The data in the List comes from the info available in the Database - workbench
        row_counter = 1
        for row in news_list:
            id = row[0]
            id_news = Label(frame, text = id, bg = "indian red", font = ('Times New Roman', 10))
            id_news.grid(row = row_counter, column = 0)
            
            
            news_date = Label(frame, text = row[1], width = 10, height = 3, borderwidth=2, relief="sunken", bg = "indian red", font = ('Times New Roman', 10))
            news_date.grid(row = row_counter, column = 1, padx = 5)
            
            news_brief = Label(frame, text = row[2], width = 100, height = 3, borderwidth=2, relief="sunken", anchor='w', justify = LEFT, wraplength = 700, bg = "indian red", font = ('Times New Roman', 10))
            news_brief.grid(row = row_counter, column = 2)
            
            news_website = Label(frame, text = row[3], width = 30, height = 3, borderwidth=2, relief="sunken", anchor='w', justify = LEFT, wraplength = 200, bg = "indian red", font = ('Times New Roman', 10), cursor="hand2")
            news_website.grid(row = row_counter, column = 3)
            news_website.bind("<Button-1>", lambda e:  webbrowser.open_new(row[3]))
            
            news_section = Label(frame, text = row[4], width = 10, height = 3, borderwidth=2, relief="sunken", anchor='w', justify = LEFT, wraplength = 100, bg = "indian red", font = ('Times New Roman', 10))
            news_section.grid(row = row_counter, column = 4)
            
            news_country = Label(frame, text = row[5], width = 10, height = 3, borderwidth=2, relief="sunken", anchor='w', justify = LEFT, wraplength = 100, bg = "indian red", font = ('Times New Roman', 10))
            news_country.grid(row = row_counter, column = 5)
            
            # Attached a button which it will delete the information from the database.
            delete = Button(frame, text = "Delete", command = lambda id = id: [DB.Saved_News.Delete_saved_news(id), 
                                                                               Prompts.Prompts.Close_Window(saves), 
                                                                               Saved_List()]
                            , bg = "indian red", anchor='w', font = ('Times New Roman', 13))
            delete.grid(row = row_counter, column = 6, padx = 5)
        
            row_counter = row_counter + 1
            
        
        saves.mainloop()