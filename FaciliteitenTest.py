import psycopg2

connection_string = "host='4.234.116.133' dbname='stationszuil' user='postgres' password='geheimpje1234'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
query_station = """ SELECT ov_bike, elevator, toilet, park_and_ride 
                       FROM station_service 
                       WHERE station_city = 'Utrecht' """
cursor.execute(query_station)
faciliteiten = cursor.fetchall()
conn.close()

for fiets in faciliteiten:
    ov_bike = f'{faciliteiten[0]}'
    gesplitst = ov_bike.strip('()').split(',')
    bike = gesplitst[1]
    if bike == 'True':
        print("There are bikes available at this station")
    else:
        print("There are no bikes at this station")
