import tkinter
from tkinter import *
import requests
import psycopg2

#---Het tonen van het weer---
api_key = "befce6c12cc4de8793e5f9de6f2ace3a"
locatie = "Utrecht"
resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q={locatie}&appid={api_key}"
response = requests.get(resource_uri)
response_data = response.json()

weather = response_data['weather'][0]['description'] #weer omschrijving
temp = response_data['main']['temp']-272.15 #temperatuur van kelvin naar ceclius

#---Pagina opstelling---
root = Tk()
root.state('zoomed')
root.configure(background='gold') #zorgt voor de iconic gele achtergrond

#---Introduction to page---
welkom = Label(master=root,
              text='Welcome to NS, Station Utrecht',
              background='white',
              foreground='dark blue',
              font=('Sans', 16, 'bold'),
              width=200,
              height=2)
welkom.pack()

#---Het weer tonen---
weer = Label(master=root,
             text='The weather today has ' + weather + ' with a temperature of ' + str(round(temp)) + ' degrees.',
             background='white',
             foreground='darkblue',
             font=('Sans', 14),
             width=150,
             height=1)
weer.pack()

#---Kop voor berichten---
berichtenlabel = Label(master=root,
               text='Messages:',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=40,
               height=2)
berichtenlabel.pack(pady=4)

#---Het laten zien van de goedgekeurde berichten, limit 5---
connection_string = "host='4.234.116.133' dbname='stationszuil' user='postgres' password='geheimpje1234'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()	# DictCursor, not the default cursor!
query_berichten = """SELECT bericht, station 
           FROM bericht 
           INNER JOIN keuring ON keuring.berichtid=bericht.berichtid 
           WHERE beoordeling = 'Ja' ORDER BY bericht.tijd DESC LIMIT 5;"""
cursor.execute(query_berichten)
records = cursor.fetchall()
conn.close()

#---Opmaak van berichten---
for record in records:
    showinglabel = Label(master=root,
                             text=f"{record[0]}, {record[1]}",
                             background='white',
                             foreground='dark blue',
                             font=('Sans', 14, 'bold'),
                             width=43,
                             height=2)
    showinglabel.pack(pady=1)
        # showinglabel.place(x=75, y=140) anchor='w'
    station = record[1]

    connection_string = "host='4.234.116.133' dbname='stationszuil' user='postgres' password='geheimpje1234'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    query_station = """ SELECT ov_bike, elevator, toilet, park_and_ride 
                       FROM station_service 
                       WHERE station_city = 'Utrecht' """
    cursor.execute(query_station)
    faciliteiten = cursor.fetchall()
    conn.close()

#---Kopje voor de faciliteiten---
faciliteitenlabel = Label(master=root,
               text='Facilities:',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=40,
               height=2)
faciliteitenlabel.pack(pady=10)

#---Fietsen op station---
for fiets in faciliteiten:
    ov_bike = f'{faciliteiten[0]}'
    gesplitst = ov_bike.strip('()').split(',')
    bike = gesplitst[0]
    if bike == 'True':
        fietsenlabel = Label(master=root,
               text='There are bikes available at this station',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=40,
               height=2)
    else:
        fietsenlabel = Label(master=root,
                             text='There are no bikes available at this station',
                             background='white',
                             foreground='dark blue',
                             font=('Sans', 16, 'bold'),
                             width=40,
                             height=2)
    fietsenlabel.pack(pady=2)
#---Liften op station---
for lifts in faciliteiten:
    elevator = f'{faciliteiten[0]}'
    gesplitst = elevator.strip('()').split(',')
    lift = gesplitst[1]
    if lift == 'True':
        liftenlabel = Label(master=root,
               text='There are elevators available at this station',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=40,
               height=2)
    else:
        liftenlabel = Label(master=root,
                             text='There are no elevators available at this station',
                             background='white',
                             foreground='dark blue',
                             font=('Sans', 16, 'bold'),
                             width=40,
                             height=2)
    liftenlabel.pack(pady=1)

#---Toiletten op station---
for toilets in faciliteiten:
    wc = f'{faciliteiten[0]}'
    gesplitst = wc.strip('(').split(',')
    toilet = gesplitst[2]
    if toilet == ' True':
        toilettenlabel = Label(master=root,
               text='There are toilets available at this station',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=40,
               height=2)
    else:
        toilettenlabel = Label(master=root,
                             text='There are no toilets available at this station',
                             background='white',
                             foreground='dark blue',
                             font=('Sans', 16, 'bold'),
                             width=40,
                             height=2)
    toilettenlabel.pack(pady=1)

#---Park&Ride op station---
for parking in faciliteiten:
    pr = f'{faciliteiten[0]}'
    gesplitst = pr.strip('(').split(',')
    park = gesplitst[2]
    if park == ' True':
        parkridelabel = Label(master=root,
               text='There is P+R available at this station',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=40,
               height=2)
    else:
        parkridelabel = Label(master=root,
                             text='There is no P+R available at this station',
                             background='white',
                             foreground='dark blue',
                             font=('Sans', 16, 'bold'),
                             width=40,
                             height=2)
    parkridelabel.pack(pady=1)





#---faciliteiten foto's---
#img = PhotoImage(file='images/img_lift.png')
#foto = Label(master=root,
             # image=img)
#foto.pack()
#foto.lift()

#---Dat de root blijft draaien---
root.mainloop()
