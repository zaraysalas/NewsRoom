# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:59:27 2021

@author: salas
"""
import requests
import News_GUI
import re
import Prompts
import time

class Connect_api():
    def search_news(default_type, year, month, day):
        # API URI
        
        pattern = re.compile("^[0-9]{2}")
        month_format = re.match(pattern, month.get())
        day_format = re.match(pattern, day.get())

        if month_format and day_format:
            c = 1
            uri = "https://newsapi.org/v2/top-headlines/sources?"
            url = uri + "category=" + default_type.get() + "&from=" + year.get() + "-" + month.get() + "-" + day.get() + "&sortBy=popularity&apiKey=1d03f5856a654a63912816b2d8377882"
            print(url)
            date = day.get() + "/" + month.get() + "/" + year.get()
            
            #Request data to the API
            request = requests.get(url)
            #Data gotten from the API
            response = request.json()
            #print(response)
            News_GUI.News_room.Delete_Widget()
            News_GUI.News_room.Header()
            #Loop to look for the "Sources" key
            for each_key in response.keys():
                if each_key == 'sources':
                    #Measure the size of the dictionary
                    lenght = len(response[each_key])
                    #print(each_key)
                    #Look into dictonary the data to show to the user
                    for i in range(lenght):
                        for key in response[each_key][i]:
                            #print(key)
                            #If the key is one of the 3 I am looking for save the information
                            if key == 'description' or key == 'url' or key == 'country' or key == 'category':
                                if key == 'description':
                                    c = c+1
                                    brief = response[each_key][i][key]
                                    #print(c)
                                    #print(brief)
                                elif key == 'url':
                                    website = response[each_key][i][key]
                                    #print(website)
                                elif key == 'category':
                                    category = response[each_key][i][key]
                                elif key == 'country':
                                    country = response[each_key][i][key]
                                    #print(country)
                                
                                    #Send the information to a function that will show it in the window.
                                    News_GUI.News_room.news_feed(c, brief, website, category, country, date)
        else:
            Prompts.Prompts.No_Number()
                