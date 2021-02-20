from haversine import haversine, Unit


neis = []
first_addresses = {}
second_addresses = {}
#write input
#first_address = (56.899699, 60.613213)
#get from database
def get_rests(filename, adds_list):
    with open(filename, "r", newline='') as file:
        for i in file.readlines():
            lat = float(i.split(';')[1][1:-1].split(',')[0])
            lng = float(i.split(';')[1][1:-1].split(',')[1])
            adds_list[str(i.split(';')[2])[:-1] + ' ' + str(i.split(';')[0])] = (lng, lat)


get_rests("burger king екатеринбург.txt", first_addresses)

get_rests("kfc екатеринбург.txt", second_addresses)
get_rests("mcdonalds екатеринбург.txt", second_addresses)

first_address = first_addresses['просп. Космонавтов, 41, Екатеринбург, Россия Бургер Кинг']
c=0
for ikey in first_addresses.keys():
    for jkey in second_addresses.keys():
        o = haversine(first_addresses[ikey], second_addresses[jkey])
        if o <= 2:
            c+=1
            # print(o, key, second_addresses[key])
    print(ikey, c)
    c=0

