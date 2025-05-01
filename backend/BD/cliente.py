from pymongo import MongoClient
from pymongo.server_api import ServerApi

cliente_pvz = MongoClient("mongodb+srv://test:test@cluster0.dhk0ch9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", server_api=ServerApi('1')).pvz

#Esto deberia de funcionar bien

