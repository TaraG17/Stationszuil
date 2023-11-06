import datetime
import random

datetimeNow = datetime.datetime.now()
date = datetimeNow.strftime("%Y/%m/%d")
time = datetimeNow.strftime("%H:%M:%S")
print(date, time)

bericht = input('Type hier uw bericht: ')
if(len(bericht)>= 140):
    print('Uw bericht is te lang')
else:
    print(bericht)

naam = input('Type hier uw naam: ')
geenNaam = 'anoniem'
if naam == '':
    print(geenNaam)
else:
    print(naam)

station = ['Utrecht', 'Amsterdam', 'Rotterdam']
randomstation = random.choice(station)

file = open("testmodule1.csv")  # opent de file
berichten = file.readlines()  # leest de file per lijn
file.close()  # sluit de file

resultaat = date + "|" + time + "|" + randomstation + " | " + str(naam) + " " + "|" + " " + str(bericht) + "\n"
#res = [date_time, randomstation, naam, bericht]


nieuw = open("testmodule1.csv", "a")  # Wijzigt de file
nieuw.write(resultaat)
nieuw.close()