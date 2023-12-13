import datetime
import psycopg2

#---Reads the file, why? No idea---
file = open("testmodule1.csv")  # opent de file
berichten = file.readlines()  # leest de file per lijn
file.close()  # sluit de file

#---Current date and time---
datetimeNow = datetime.datetime.now()
date = datetimeNow.strftime("%Y/%m/%d")
time = datetimeNow.strftime("%H:%M:%S")
print(date, time)

#---Input Moderator---
naam = input("Geef je naam: ")
email = input("Geef je mailadres: ")
# inlog naam + email van de moderator
# datum van moderator

#---Ton of code for moderating system---
for bericht in berichten:
    gesplitst = bericht.strip().split('|')
    while True:
        keuring = input("Is dit bericht goedgekeurd:" + gesplitst[4] + "\n" + " Ja/Nee: ")
        if keuring == "Ja" or keuring == "Nee":
            #---Connection database---
            connection_string = "host='4.234.116.133' dbname='stationszuil' user='postgres' password='geheimpje1234'"
            conn = psycopg2.connect(connection_string) #maakt connectie met Database
            cursor = conn.cursor()

            #---Query Message---
            query_bericht = """INSERT INTO Bericht(naam, bericht, datum, tijd, station) VALUES (%s, %s, %s, %s, %s) RETURNING berichtid;"""
            data_bericht = (gesplitst[3], gesplitst[4], gesplitst[0], gesplitst[1],gesplitst[2]) #zet het in de juiste volgorde
            cursor.execute(query_bericht, data_bericht)
            berichtid = cursor.fetchone()[0] #pakt de eerste rij, eerste nummer
            #---Query Moderator---
            query_moderator = """INSERT INTO Moderator(naam, email) VALUES (%s, %s) RETURNING moderatorid;"""
            data_moderator = (naam, email)
            cursor.execute(query_moderator, data_moderator)
            moderatorid = cursor.fetchone()[0] #pakt de eerste rij, eerste nummer
            #---Query Approval---
            query_keuring = """INSERT INTO Keuring(moderatorid, berichtid, beoordeling, datum, tijd) VALUES (%s, %s, %s, %s, %s);"""
            data_keuring = (moderatorid, berichtid, keuring, date, time)
            cursor.execute(query_keuring, data_keuring)

            conn.commit()
            conn.close()
            break
#---Empties the file after approval---
file = open("testmodule1.csv", "w")  # opent de file
file.write("")
file.close()  # sluit de file
