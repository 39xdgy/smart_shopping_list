from pymongo import MongoClient
import certifi
conn = MongoClient("mongodb+srv://Admin:test_admin@cluster0.kghzn8n.mongodb.net/test", tlsCAFile=certifi.where()) #TODO: ISSUE