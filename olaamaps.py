print('CONNECTING OLA MAPS')
from keys import *
import math
client = get_clientMaps()
pin1 = input("Enter Tool booth address with pin")
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences in coordinates
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance

def haversineDist(pin2):

    global lng1, lat1, lat2, lng2
    results = client.geocode(pin1)

    if results:
        location = results[0]['geometry']['location']
        lat1 = location['lat']
        lng1 = location['lng']

    else:
        print("No results found.")

    results = client.geocode(pin2)

    if results:
        location = results[0]['geometry']['location']
        lat2 = location['lat']
        lng2 = location['lng']

    else:
        print("No results found.")

    return haversine(lat1, lng1, lat2, lng2)




pin2 = "hosa hwerwatta kumata 581332"
ndistance = haversineDist(pin2)
if ndistance >0:
    # print(ndistance)
    print('OLA MAPS CONNECTED SUCCESSFUL')




# while True:
#
#     pin2 = input("Enter pin 2")



