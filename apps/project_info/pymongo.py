from pymongo import MongoClient

username = 'mongo'
password = 'Jk4qO6HHR6eGQQGxlftt'

client = MongoClient(
    'mongodb://mongo:********@containers-us-west-67.railway.app:7017', username=username, password=password)
db = client['human_microbiome']

collection = db["project_info"]