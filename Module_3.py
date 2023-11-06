from tkinter import *
import requests
import psycopg2

api_key = "befce6c12cc4de8793e5f9de6f2ace3a"
locatie = "Utrecht"
resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q={locatie}&appid={api_key}"
response = requests.get(resource_uri)
response_data = response.json()

weather = response_data['weather'][0]['description'] #weer omschrijving
temp = response_data['main']['temp']-272.15 #temperatuur van kelvin naar ceclius

pagina = Tk()
pagina.state('zoomed') #zorgt voor fullscreen

pagina.configure(background='gold')

welkom = Label(master=pagina,
              text='Welcome to NS',
              background='white',
              foreground='dark blue',
              font=('Sans', 16, 'bold'),
              width=200,
              height=2)
welkom.pack()

weer = Label(master=pagina,
             text='The weather today has ' + weather + ' with a temperature of ' + str(round(temp)) + ' degrees.',
             background='white',
             foreground='darkblue',
             font=('Sans', 14),
             width=150,
             height=1)
weer.pack(side='top', anchor=CENTER)

img = PhotoImage(file='images/img_lift.png')
foto = Label(master=pagina,
              image=img)
foto.pack()

berichtenlabel = Label(master=pagina,
               text='Messages:',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=50,
               height=2)
berichtenlabel.pack(anchor='w', pady=10)


connection_string = "host='4.234.116.133' dbname='stationszuil' user='postgres' password='geheimpje1234'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()	# DictCursor, not the default cursor!
query = """SELECT bericht, station 
           FROM bericht 
           INNER JOIN keuring ON keuring.berichtid=bericht.berichtid 
           WHERE beoordeling = 'Ja' LIMIT 5;"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

for record in records:
    showinglabel = Label(master=pagina,
               text=f"{record[0]} , {record[1]}",
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=50,
               height=2)

    showinglabel.pack(side='top',
                      anchor='w',
                      pady=2)
    station = record[1]

    connection_string = "host='4.234.116.133' dbname='stationszuil' user='postgres' password='geheimpje1234'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    querystation = """ SELECT ov_bike, elevator, toilet, park_and_ride 
                       FROM station_service 
                       WHERE station_city = 'Rotterdam' """
    cursor.execute(querystation)
    records = cursor.fetchall()
    conn.close()


faciliteitenlabel = Label(master=pagina,
               text='Facilities:',
               background='white',
               foreground='dark blue',
               font=('Sans', 16, 'bold'),
               width=50,
               height=2)
faciliteitenlabel.pack(anchor='e')


pagina.mainloop()
