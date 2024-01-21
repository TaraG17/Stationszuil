import datetime
import random

#---Current time---
datetimeNow = datetime.datetime.now()
date = datetimeNow.strftime("%Y/%m/%d")
time = datetimeNow.strftime("%H:%M:%S")
print(date, time)

#---User input for message---
while True:
    bericht = input('Type hier uw bericht: ')
    if len(bericht) >= 140: # als het bericht langer is dan 140 karakters, moet de user opnieuw een bericht intypen
        print('Uw bericht is te lang. Probeer opnieuw.')
    else:
        break # zodra de user een bericht intypt wat kleiner is dan 140 karakters, wordt de loop verbroken

print('Je kan dit volgende veld leeg laten om anoniem te blijven')
naam = input('Type hier uw naam: ')
geenNaam = 'Anoniem'
if naam == '':
    print(geenNaam)

#---Randomizing station per message---
station = ['Utrecht', 'Amsterdam', 'Rotterdam']
randomstation = random.choice(station) # kiest een random station uit

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

