# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 19:55:00 2021

@author: zaray salas lopez
"""
import time
import API
import DB
import Saves_GUI
import Prompts
import webbrowser

from tkinter import *

class News_room():
    def __init__(self):
    # -------- News Room window --------------------------------
    # Function to run when the button "GO TO NEWS ROOM" is pressed
        
        # ...then open the News Room Window.
        global news_room_window
        news_room_window = Tk()
        news_room_window.geometry("1275x400+50+50")
        
        news_room_window.title("N E W S   R O O M - Zaray Salas Lopez")
  
        frame1 = Canvas(news_room_window, bg = "#006699")
                
        # Run function to get the image
        global png_bg
        png_bg = Prompts.Prompts.image_background(1300, 1000, news_room_window, frame1)
        # Set image as background
        frame1.create_image(0,0,image = png_bg, anchor = 'nw')
        
        
        frame1.pack(expand = FALSE, fill = BOTH)
        
        # Variable with the API key
        api_key = '1d03f5856a654a63912816b2d8377882'
        
        # Select news category
        label_type = Label (frame1, text = "NEWS TYPE: ", bg = "#006699", font = ('Times New Roman', 11), foreground = "white")
        label_type.grid(row = 0, column = 1)
        news_options = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        global news_type
        news_type = StringVar()
        news_type.set(news_options[0])
        news_type_drop = OptionMenu (frame1, news_type, *news_options)
        news_type_drop.configure(width = 15)
        news_type_drop.grid(row = 0, column = 2, padx = 10)
                
        # By default show today's news. The month and year can be change
        label_date = Label (frame1, text = "DATE (YYYY-MM-DD): ", bg = "#006699", font = ('Times New Roman', 11), foreground = "white")
        label_date.grid(row = 0, column = 3, pady = 25)
        global year
        textEntry = StringVar()
        textEntry.set(time.strftime("%Y"))
        # The year can not be change due to the API's data availability. Current year can be only consulted.
        year = Entry(frame1, width = 6, textvariable = textEntry, state='disabled')
        year.grid(row = 0, column = 4)
        
        # Month and day can be change
        global month
        month = Entry(frame1, width = 5)
        month.grid(row = 0, column = 5)
        month.insert(0,time.strftime("%m"))
        
        global day
        day = Entry(frame1, width = 5)
        day.grid(row = 0, column = 6)
        day.insert(0,time.strftime("%d"))
        
        # When the button is pressed the request is send to the API and the data returned is showed in the lower section.
        search_news_button = Button (frame1, text = "SEARCH NEWS", command = lambda: API.Connect_api.search_news (news_type, year, month, day), foreground ="#006699", font = ('Times New Roman', 9))
        search_news_button.grid(row = 0, column = 7, padx = 10)
        
        # Pressing this button display a new window with the news previosly saved.
        go_list = Button (frame1, text = "GO NEWS SAVED", command = lambda: Saves_GUI.Saved_List(news_room_window)
                          , foreground ="#006699", font = ('Times New Roman', 9))
        go_list.grid(row = 0, column = 8, padx = 100)
        
        global frame3
        frame3 = Canvas(news_room_window, bg = "#006699")
        frame3.pack(expand = 'y', fill = BOTH)
        frame3.create_image(0,-65,image = png_bg, anchor = 'nw')
        #--------------Setting the Right scrollbar---------------------------
        global wraper
        wraper = LabelFrame(news_room_window)
        
        global canvas
        canvas = Canvas(wraper)
        canvas.pack(side = LEFT, fill = 'both', expand = 'yes')
        
        global scrollbar
        scrollbar = Scrollbar(wraper, orient = 'vertical', command = canvas.yview)
        scrollbar.pack(side = RIGHT, fill = 'y')
        
        news_room_window.mainloop()
        
    def Header():
        canvas.configure(yscrollcommand = scrollbar.set)
        
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))

        global frame2
        # Clean the frame
        frame3.destroy()
        frame2 = Canvas(canvas, bg = "#006699")
        frame2.create_image(0,0,image = png_bg, anchor = 'nw')
        canvas.create_window((0,0), window = frame2, anchor = 'nw')
        
        wraper.pack(fill = 'both', expand = 'yes')
                        
        # Show the section and date where the data comes from
        news_label = Label(frame2, text = (news_type.get()).upper() + " NEWS FEED FROM " + day.get() + " / " + month.get() + " / " + year.get(), bg = "#006699", font = ('Times New Roman', 35), anchor = 'n', foreground = "white")
        news_label.grid(row = 0, column = 0, columnspan = 6, pady = 15)
        # Labels for the columns
        news_num = Label(frame2, text = "NUM", bg = "#006699", font = ('Times New Roman', 0)).grid(row = 1, column = 0)
        news_brief = Label(frame2, text = "BRIEF", bg = "#006699", font = ('Times New Roman', 0)).grid(row = 1, column = 1)
        news_website = Label(frame2, text = "WEBSITE", bg = "#006699", font = ('Times New Roman', 0)).grid(row = 1, column = 2)
        news_section = Label(frame2, text = "SECTION", bg = "#006699", font = ('Times New Roman', 0)).grid(row = 1, column = 3)
        news_country = Label(frame2, text = "COUNTRY", bg = "#006699", font = ('Times New Roman', 0)).grid(row = 1, column = 4) 
            
    #Take the info colected from the API's request and show it to the user
    def news_feed(c, brief, website, category, country, date):
        news_num = Label(frame2, text = c-1, bg = "#006699", font = ('Times New Roman', 10)).grid(row = c, column = 0)
        
        news_brief = Label(frame2, text = brief, width = 100, height = 3, borderwidth=2, relief="sunken", anchor='w', justify = LEFT, wraplength = 700, bg = "#006699", font = ('Times New Roman', 10))
        news_brief.grid(row = c, column = 1, padx = 5)
        
        news_website = Label(frame2, text = website, width = 30, height = 3, borderwidth=2, relief="sunken", anchor='w', justify = LEFT, wraplength = 200, bg = "#006699", font = ('Times New Roman', 10), cursor="hand2")
        news_website.grid(row = c, column = 2)
        news_website.bind("<Button-1>", lambda e:  webbrowser.open_new(website))
        
        news_section = Label(frame2, text = category, width = 10, height = 3, borderwidth=2, relief="sunken", anchor='w', justify = LEFT, wraplength = 100, bg = "#006699", font = ('Times New Roman', 10))
        news_section.grid(row = c, column = 3)
        
        news_country = Label(frame2, text = country, width = 10, height = 3, borderwidth=2, relief="sunken", anchor='w', justify = LEFT, wraplength = 100, bg = "#006699", font = ('Times New Roman', 10))
        news_country.grid(row = c, column = 4)

        # Set a checkbox which if it is tick, it will connect to the database and save the info.
        bool_var = BooleanVar()
        save = Checkbutton(frame2, text = "Save", command = lambda: DB.Saved_News.Your_News(bool_var, date, brief, website, country, category), variable=bool_var, bg = "#006699", anchor='w', font = ('Times New Roman', 13))
        save.grid(row = c, column = 5, padx = 5)
    
    # Clean the canvas so the next batch of widgets can be place in
    def Delete_Widget():
        for widget in canvas.winfo_children():
            widget.destroy()