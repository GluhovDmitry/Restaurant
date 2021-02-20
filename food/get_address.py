import requests
from .key import api_key

api_key = api_key

organization = "burger king екатеринбург"


def get_address(org):
    url = f"https://search-maps.yandex.ru/v1/?apikey={api_key}&text={org}&lang=ru_RU&results=100"
    result = requests.get(url).json()
    filename = str(org)+'.txt'
    with open(filename, "w", newline='') as file:
        for i in result['features']:
            file.write(str(i['properties']['name']) +';'+ str(i['geometry']['coordinates'])+';'
                       +str(i['properties']['description'])+ "\n")

print(get_address(organization))