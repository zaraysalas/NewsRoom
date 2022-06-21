# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 01:33:21 2021

@author: salas
"""
import mysql.connector
import ctypes
import DB_GUI
import Prompts
import News_GUI

class Saved_News():
    
    #Catching the data about the news which the user want to save.
    def Your_News(bool_var, date, brief, website, country, section):
              
        chosen = dict()
        # If the checkbox was ticked (true), the function saves the info in a dictionary
        if bool_var.get():
            chosen['date'] = date
            chosen['brief'] = brief
            chosen['website'] = website
            chosen['section'] = section
            chosen['country'] = country

            Saved_News.Save_chosen_news(chosen)
    
    # Save the parameters from the mini-window at the start called DB_GUI
    def Parameters(h, po, u, pa):
        global hostname
        global port
        global username
        global password
        
        hostname = h.get()
        port = po.get()
        username = u.get()
        password = pa.get()
        
    
    # Return a connection with workbench to be used in other functions.
    def Connect():
        try:
            connection = mysql.connector.connect(host = hostname,
                                      port = port,
                                      user = username,
                                      password = password)
        
            return connection
        # If it does not connect, gives an error message explaining that the parameters where not given when asked for.
        except:
            Prompts.Prompts.No_Parameters()
    
    # Create a databasea nd table
    def Create_DB():
        connection = Saved_News.Connect()
        try:
            
            data = connection.cursor()
            # Create a database called news_list
            query = "CREATE DATABASE news_list;"
            data.execute(query)
            query = "USE news_list;"
            data.execute(query)
            # Create the table
            query = "CREATE TABLE news_list.chosen(ID  int NOT NULL UNIQUE AUTO_INCREMENT, DATE VARCHAR(255) NOT NULL, BRIEF VARCHAR(255) NOT NULL, WEBSITE VARCHAR(255) NOT NULL, SECTION VARCHAR(255) NOT NULL, COUNTRY VARCHAR(255) NOT NULL, PRIMARY KEY(ID));"
            data.execute(query)
            # Stick the modification to the database
            connection.commit()
            connection.close()
        except:            
            connection.close()
    
    def Save_chosen_news(chosen):
        connection = Saved_News.Connect()
        
        data = connection.cursor()
        # Insert the news that the user wants to save, excluding all than the brief, website, section and country
        query = "INSERT INTO news_list.chosen(DATE, BRIEF, WEBSITE, SECTION, COUNTRY) VALUES('" + chosen['date'] + "', '" + chosen['brief'] + "', '" + chosen['website'] +  "', '" + chosen['section'] +  "', '" + chosen['country'] + "');"
        
        data.execute(query)
        connection.commit()  
        connection.close()
    
    def Retrive_saved_news(news_room_window, saves):
        try:
            connection = Saved_News.Connect()
            
            data = connection.cursor()
            
            # Takes all the informaqtion available in the table news_list
            query = "SELECT * FROM news_list.chosen;"
            
            data.execute(query)
            # Create a List for saving the table
            news_list = list()
            # Run a for loop to save every row available in the List
            for row in data:
                news_list.append(row)
    
            connection.close()
            Prompts.Prompts.Close_Window(news_room_window)
            return news_list
        except:
            Prompts.Prompts.Close_Window(saves)
            print("nothing")
    
    # Function to delete a row at the time in the database base in the ID as a PRIMARY KEY
    def Delete_saved_news(id):
        connection = Saved_News.Connect()
        
        data = connection.cursor()
        
        query = "DELETE FROM news_list.chosen WHERE ID = '"+ str(id) + "';"
        
        data.execute(query)
        connection.commit()
        connection.close()