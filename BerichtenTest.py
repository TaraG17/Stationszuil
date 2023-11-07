import psycopg2

connection_string = "host='localhost' dbname='StationZuil' user='Taartje' password='geheimpje123'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()	# DictCursor, not the default cursor!
query = """SELECT bericht, naam FROM bericht INNER JOIN keuring on keuring.berichtid=bericht.berichtid WHERE beoordeling = 'Ja';"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

for record in records:
    print(record[0])
