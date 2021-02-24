'''

This code connecting to database, then with function get_address
gets restaurants from yandex api and puts them into database

Код подключается к БД и с помощью функции get_address получает
точки и адреса ресторанов по яндекс api и складывает их БД

Этот код не учавтсует в работе приложения, его запуск лишь заполняет БД

В задании было указано получить данные с оф сайтов,
но сайты предоставляют данные через те же яндекс карты,
подход с yandex api показался мне вполне адекватным.

Также, в задании не указан регион поиска ресторанов, поэтому он ограничен Екатеринбургом.
При желании его легко можно раширить (ограничение api запроса - 500 ресторанов).

'''
from .key import pword
import psycopg2
import requests
from key import api_key

conn = psycopg2.connect(dbname='django_db', user='dima', password=f'{pword}', host='127.0.0.1', port='5432')

cursor = conn.cursor()
api_key = api_key

organization1 = "burgerking"
organization2 = "mcdonalds"
organization3 = "kfc"


def get_address(org):
    #   concatenate string (to choose search region)
    text = str(org) + ' екатеринбург'
    url = f"https://search-maps.yandex.ru/v1/?apikey={api_key}&text={text}&lang=ru_RU&results=500"
    result = requests.get(url).json()
    for i in result['features']:
        lat = float(str(i['geometry']['coordinates'])[1:-1].split(',')[0])
        lng = float(str(i['geometry']['coordinates'])[1:-1].split(',')[1])
        name = str(i['properties']['name'])
        address = str(i['properties']['description'])
        table = 'food_' + str(org)
        cursor.execute(f"INSERT INTO {table} (name, lat, lng, address) "
                       f"VALUES ('{name}', {lat}, {lng}, '{address}');")


get_address(organization1)
get_address(organization2)
get_address(organization3)

conn.commit()
cursor.close()
conn.close()
