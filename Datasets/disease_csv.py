import csv
from pymongo import MongoClient

username = 'mongo'
password = 'Jk4qO6HHR6eGQQGxlftt'

client = MongoClient(
    'mongodb://mongo:********@containers-us-west-67.railway.app:7017', username=username, password=password)
db = client['human_microbiome']

collection = db['disease_info']

# Read CSV file
with open('disease.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    # Create counter for _id field
    counter = 1

    # Insert each row into MongoDB collection
    for row in reader:
        row['_id'] = counter
        collection.insert_one(row)
        print(counter)  
        counter += 1

print("Done!")

# Close MongoDB connection
client.close()
