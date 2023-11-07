# Stationszuil
Opdracht: Bouw een stationszuil die het mogelijk maakt voor reizigers om berichten achter te laten op een station, waarbij goedgekeurde berichten in de stationshal worden getoond voor alle andere reizigers.
Het systeem (de stationszuil) bestaat uit drie modules:

Module 1: Zuil
Module 2: Moderatie
Module 3: Stationshalscherm

De stationszuil moet gerealiseerd worden in Python. De architectuur van het systeem staat geschetst in onderstaand figuur. 
Vanuit de module 'Zuil' worden gegevens weggeschreven in een tekstbestand. 
In de module 'Moderatie' worden de gegevens uit het tekstbestand gelezen, aangevuld met moderator gegevens en dan weggeschreven naar een PostgreSQL-database. 
De module 'Stationsscherm' leest gegevens uit de database en 'leest' gegevens van Open Weather Map via een API-koppeling.
