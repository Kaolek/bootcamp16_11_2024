from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
uri = "mongodb+srv://rajkonkret660:2zkqLAEqgsle90O3@cluster0.pjuh61y.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)
