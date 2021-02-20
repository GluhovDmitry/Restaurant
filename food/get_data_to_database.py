import psycopg2
import requests
from key import api_key

conn = psycopg2.connect(dbname='django_db', user='dima', password='1', host='127.0.0.1', port='5432')

cursor = conn.cursor()
api_key = api_key

organization1 = "burger_king"
organization2 = "mcdonalds"
organization3 = "kfc"

def get_address(org):
    text = str(org)+' екатеринбург'
    url = f"https://search-maps.yandex.ru/v1/?apikey={api_key}&text={text}&lang=ru_RU&results=100"
    result = requests.get(url).json()
    for i in result['features']:
        lat = float(str(i['geometry']['coordinates'])[1:-1].split(',')[0])
        lng = float(str(i['geometry']['coordinates'])[1:-1].split(',')[1])
        name = str(i['properties']['name'])
        address = str(i['properties']['description'])
        table = 'food_'+str(org)
        cursor.execute(f"INSERT INTO {table} (name, lat, lng, address) "
                       f"VALUES ('{name}', {lat}, {lng}, '{address}');")

get_address(organization1)
get_address(organization2)
get_address(organization3)

conn.commit()
cursor.close()
conn.close()




