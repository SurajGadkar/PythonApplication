# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:49:44 2020

@author: Suraj Gadkar
"""

import tkinter as tk
from tkinter import font
import requests

Height = 700
Width = 600

def format_response(jsonResponse):
	name = jsonResponse['name']
	desc = jsonResponse['weather'][0]['description']
	temp = jsonResponse['main']['temp']
	return '\n City : '+ name + '\n Conditions : ' + desc + '\n Temperature : ' + str(temp)

def error_response(jsonResponse):
	errorMSG = jsonResponse['message']
	return '\n ERROR : ' + errorMSG

def getWeather(city):
	try:
		weather_api_key = '5492d4a2b855717bf588e6fb5edb5666'
		api_url = 'https://api.openweathermap.org/data/2.5/weather?'
		params = {'APPID' : weather_api_key, 'q' : city,  'units' : 'metric'}
		response = requests.get(api_url, params = params)
		jsonResponse = response.json()
		label['text'] = format_response(jsonResponse)

	except:
		label['text'] = error_response(jsonResponse)
	

root = tk.Tk()

canvas = tk.Canvas(root, height = Height, width = Width)
canvas.pack()

background_img = tk.PhotoImage(file = 'background.png')
background_label = tk.Label(root, image = background_img)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

bottomFrame = tk.Frame(root, bg = 'blue', bd = 5)
bottomFrame.place(relx = 0.05, rely =  0.4, relwidth = 0.9, relheight = 0.55)

topFrame = tk.Frame(root, bg = 'gray', bd = 10)
topFrame.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.2)

topEntry = tk.Entry(topFrame, bg = 'white')
topEntry.place(relx = 0.05, rely = 0.35,relwidth = 0.6, relheight = 0.3)

button = tk.Button(topFrame, text = 'Check Weather', bg = 'black', fg = 'white', command = lambda: getWeather(topEntry.get()))
button.place(relx = 0.75, rely = 0.35, relwidth = 0.2, relheight = 0.3)

label = tk.Label(bottomFrame, bg = 'gray', font = ('Montserrat', 20))
label.place(relwidth = 1, relheight = 1)

root.mainloop()


