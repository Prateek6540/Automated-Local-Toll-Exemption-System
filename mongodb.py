
from keys import *
from olaamaps import *
print('Connecting mongoDB')
myclient = get_DBClient()
mydb = myclient['yourDatabaseName']
mycol = mydb['vehical_details']
print('Connected MongoDB sucessfully')


myDist = mydb['distance']


def add_Dist(distance,number):
    query = {"_id":number}
    if myDist.find_one(query) is None:
        new_document = {
            "_id": number,
            "distance": distance
        }
        myDist.insert_one(new_document)
    return myDist.find_one(query)['distance']



def findDist(number):
    query = {"_id": number}
    dist = None
    dist = myDist.find_one(query)
    if dist is None:
        if mycol.find_one(query) is not None:
            #here it is required to call the api of praivahan to get the details. but as the i exhausted the hits \
            #i have created the data base with the mongoDB with some veihcal details..

            pin2 = mycol.find_one(query)['permAddress']
            print(pin2)
            distance = haversineDist(pin2)
            print(distance)
            return add_Dist(distance,number)
        return None
    return dist['distance']



# add_Dist(15,"KL48P6214")
# print(findDist("KA47V9173"))

# print(mydb.list_collection_names())
# while True:
#     rc = input("Enter RC")
#     add = input("enter address")
#     mydict = {
#
#     }
#     query = {"_id": rc}
#     x = mycol.find_one(query)
#     if x is None:
#         mycol.insert_one(mydict)