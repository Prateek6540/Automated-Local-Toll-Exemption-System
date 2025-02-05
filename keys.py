import os
from dotenv import load_dotenv
from olamaps import Client
import pymongo
load_dotenv()

def get_clientMaps():
    return Client(api_key=os.getenv("OLAMAPS_API_KEY"))

def get_DBClient():
    return pymongo.MongoClient(os.getenv("MONGO_URI"))

# def get_DBClient():
#
#     try:
#         client = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
#         client.admin.command('ping')  # Check if the connection is successful
#         print("MongoDB connection established!")
#         return client
#     except pymongo.errors.ConfigurationError as e:
#         print(f"Configuration error: {e}")
#     except pymongo.errors.ServerSelectionTimeoutError as e:
#         print(f"Server selection timeout: {e}")
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#     return None
