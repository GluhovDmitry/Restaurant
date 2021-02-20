from haversine import haversine
import psycopg2


#adrs = 'ул. Вайнера, 72, Екатеринбург, Россия'


def count_distance(db_name, address):
    conn = psycopg2.connect(dbname='django_db', user='dima', password='1', host='127.0.0.1', port='5432')
    cursor = conn.cursor()
    competitors = []
    cursor.execute(f"SELECT lat, lng FROM food_burger_king WHERE address = '{address}'")
    coordinates = cursor.fetchone()
    bk_lat = coordinates[0]
    bk_lng = coordinates[1]

    cursor.execute(f"SELECT * FROM {db_name};")
    for row in cursor:
        mc_lat = row[2]
        mc_lng = row[3]
        distance = haversine((bk_lng, bk_lat), (mc_lng, mc_lat))
        if distance <= 2:
            competitors.append((row, distance))

    cursor.close()
    conn.close()
    return competitors
'''
c = []
c += count_distance('food_mcdonalds', adrs)
c+= count_distance('food_kfc', adrs)
for row in c[0:]:
    print(row[0][4])
print(len(c))
#print(c[0:])
c.clear()
'''

