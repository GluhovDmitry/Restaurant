'''

This code connects to database then selects longitude and latitude of the chosen point.
Then it iterates through competitors restaurants and calculates distance with haversine (distance < 2 km).

Код ведет подключение к БД и извлекает долготу и широту выбранной точки.
Затем итерируется по ресторанам конкурентов и подсчитывает расстояние между точками при помощи модуля haversine.

'''


from haversine import haversine
import psycopg2


# adrs = 'ул. Вайнера, 72, Екатеринбург, Россия'


def count_distance(table_name, address):
    conn = psycopg2.connect(dbname='django_db', user='dima', password='1', host='127.0.0.1', port='5432')
    cursor = conn.cursor()
    competitors = []
    cursor.execute(f"SELECT lat, lng FROM food_burgerking WHERE address = '{address}'")
    coordinates = cursor.fetchone()
    bk_lat = coordinates[0]
    bk_lng = coordinates[1]

    cursor.execute(f"SELECT * FROM {table_name};")

#   iterate in competitors restaurants
    for row in cursor:
        mc_lat = row[2]
        mc_lng = row[3]
        distance = haversine((bk_lng, bk_lat), (mc_lng, mc_lat))
        if distance <= 2:
            competitors.append((row, distance))

    cursor.close()
    conn.close()
    return competitors


