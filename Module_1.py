import datetime
import random

#---Current time---
datetimeNow = datetime.datetime.now()
date = datetimeNow.strftime("%Y/%m/%d")
time = datetimeNow.strftime("%H:%M:%S")
print(date, time)

#---User input for message---
bericht = input('Type hier uw bericht: ')
if(len(bericht)>= 140):
    print('Uw bericht is te lang')
else:
    print(bericht)

print('Laat dit veld leeg om anoniem te blijven')
naam = input('Type hier uw naam: ')
geenNaam = 'anoniem'
if naam == '':
    print(geenNaam)
else:
    print(naam)

#---Randomizing station per message---
station = ['Utrecht', 'Amsterdam', 'Rotterdam']
randomstation = random.choice(station)

#---Reading file---
file = open("testmodule1.csv")  # opent de file
berichten = file.readlines()  # leest de file per lijn
file.close()  # sluit de file

#---String of total data that has to be written to file---
resultaat = date + "|" + time + "|" + randomstation + " | " + str(naam) + " " + "|" + " " + str(bericht) + "\n"
#res = [date_time, randomstation, naam, bericht]

#---Adds information to file---
nieuw = open("testmodule1.csv", "a")  # Wijzigt de file
nieuw.write(resultaat)
nieuw.close()
