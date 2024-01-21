import tkinter
from tkinter import *
import requests
import psycopg2
from functools import partial

#---Welcome message customizable per Station using button---
def onclick(message):
    global fac_frame
    welkom.config(text='Welcome to NS, Station ' + message)
    locatie = message #Depending on button for designated station

    #---Showing the weather for the specific station---
    api_key = "befce6c12cc4de8793e5f9de6f2ace3a"
    resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q={locatie}&appid={api_key}"
    response = requests.get(resource_uri)
    response_data = response.json()

    weather = response_data['weather'][0]['description'] #Weather description from API
    temp = response_data['main']['temp']-272.15 #Calculates the temp from fahrenheit to celcius
    weer.config(text='The weather today has ' + weather + ' with a temperature of ' + str(round(temp)) + ' degrees.')

    # ---Connection with the Database for facilities---
    connection_string = "host='4.234.116.133' dbname='stationszuil' user='postgres' password='geheimpje1234'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    query_station = """ SELECT ov_bike, elevator, toilet, park_and_ride 
                           FROM station_service 
                           WHERE station_city = %s """
    cursor.execute(query_station, (locatie,)) #Does the facilities per station
    faciliteiten = cursor.fetchone()  #Grabs the row
    conn.close()

#---If Frame exists, then destroys---
    if fac_frame:
        fac_frame.destroy()

#---Frame for the facilities---
    fac_frame = Frame(master=root, background='gold') #Seperate frame so that the labels don't get doubled
    fac_frame.pack()

    # ---Header for facilities---
    faciliteitenlabel = Label(master=fac_frame,
                              text='Facilities:',
                              background='white',
                              foreground='dark blue',
                              font=('Sans', 16, 'bold'),
                              width=40,
                              height=2)
    faciliteitenlabel.pack(pady=10)

    # ---Facilities at designated station---
    bike, elevator, toilet, parkride = faciliteiten
    if faciliteiten:
        # ---Bikes---
        if bike:
            fietsenlabel = Label(master=fac_frame,
                                 text='There are bikes available at this station',
                                 background='white',
                                 foreground='dark blue',
                                 font=('Sans', 16, 'bold'),
                                 width=40,
                                 height=2)
            fietsenlabel.pack(pady=2)
        # ---Elevators---
        if elevator:
            liftenlabel = Label(master=fac_frame,
                                text='There are elevators available at this station',
                                background='white',
                                foreground='dark blue',
                                font=('Sans', 16, 'bold'),
                                width=40,
                                height=2)
            liftenlabel.pack(pady=1)
        # ---Toilets---
        if toilet:
            toilettenlabel = Label(master=fac_frame,
                                   text='There are toilets available at this station',
                                   background='white',
                                   foreground='dark blue',
                                   font=('Sans', 16, 'bold'),
                                   width=40,
                                   height=2)
            toilettenlabel.pack(pady=1)
        # ---Park and Ride---
        if parkride:
            parkridelabel = Label(master=fac_frame,
                                  text='There is P+R available at this station',
                                  background='white',
                                  foreground='dark blue',
                                  font=('Sans', 16, 'bold'),
                                  width=40,
                                  height=2)
            parkridelabel.pack(pady=1)

#---Page Setup---
root = Tk()
root.state('zoomed') #Fullscreen
root.configure(background='gold') #Provides the iconic yellow background

#---Introduction to Page | Head Title---
welkom = Label(master=root,
              text='Welcome to NS',
              background='white',
              foreground='dark blue',
              font=('Sans', 16, 'bold'),
              width=200,
              height=2)
welkom.pack()

#---Buttons for different Stations---
button_style = {
    "background": "white", #Colour of button
    "foreground": "darkblue", #Colour of font
    "activebackground": "grey", #Colour when pressed
    "activeforeground": "darkblue", #Colour of font when pressed
    "font": ('Sans', 10, 'bold'), #Font style
    "relief": "raised", #Style of button
    "pady": 2} #Thickness

button_Amsterdam = Button(master=root, text='Station Amsterdam', command=partial(onclick, "Amsterdam"), **button_style)
button_Amsterdam.place(relx=1, x=-10, y=10, anchor='ne') #Placement
button_Amsterdam.lift() #Lifting to the foreground

button_Utrecht = Button(master=root, text='Station Utrecht', command=partial(onclick, "Utrecht"),**button_style)
button_Utrecht.place(relx=1, x=-10, y=40, anchor='ne')
button_Utrecht.lift()

button_Rotterdam = Button(master=root, text='Station Rotterdam', command=partial(onclick, "Rotterdam"),**button_style)
button_Rotterdam.place(relx=1, x=-10, y=70, anchor='ne')
button_Rotterdam.lift()

#---Showing the weather---
weer = Label(master=root,
             background='white',
             foreground='darkblue',
             font=('Sans', 14),
             width=150,
             height=1)
weer.pack()
weer.lower() #So that the white does not overlap the buttons

#---Header for messages---
berichtenlabel = Label(master=root,
               text='Messages:',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=40,
               height=2)
berichtenlabel.pack(pady=4)

#---Displaying the approved messages, limit 5---
connection_string = "host='4.234.116.133' dbname='stationszuil' user='postgres' password='geheimpje1234'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()	# DictCursor, not the default cursor!
query_berichten = """SELECT bericht, station 
           FROM bericht 
           INNER JOIN keuring ON keuring.berichtid=bericht.berichtid 
           WHERE beoordeling = 'Ja' ORDER BY bericht.tijd + bericht.datum DESC LIMIT 5;""" #Limiting the last 5 messages
cursor.execute(query_berichten)
records = cursor.fetchall()
conn.close()

#---Formatting messages---
for record in records:
    showinglabel = Label(master=root,
                             text=f"{record[0]}, {record[1]}", #Text that shows the message with the random station
                             background='white',
                             foreground='dark blue',
                             font=('Sans', 14, 'bold'),
                             width=43,
                             height=2)
    showinglabel.pack(pady=1)
    station = record[1]

#---Frame for Facilities---
fac_frame = Frame(master=root, background='gold')

#---That the root remains running---
root.mainloop()
