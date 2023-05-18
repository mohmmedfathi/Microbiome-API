import csv
from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['test_db']
# # collection_names = db.list_collection_names()

username = 'mongo'
password = 'Jk4qO6HHR6eGQQGxlftt'

client = MongoClient(
    'mongodb://mongo:********@containers-us-west-67.railway.app:7017', username=username, password=password)
db = client['human_microbiome']

collection_names = db.list_collection_names()
print(collection_names)

human = db["human_info"]
project = db["project_info"]

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    counter = 0
    # Skip the header row
    next(reader)
    for row in reader:

        first_five_fields = {
            '_id': counter,
            'HMP_ID': row[0],
            'GOLD_ID': row[1],
            'Organism_Name': row[2],
            'Domain': row[3],
            'NCBI_Superkingdom': row[4],
            'HMP_Isolation_Body_Site': row[5]
        }

        remaining_fields = {
            'Human_id': counter,
            'Project_Status': row[6],
            'NCBI Current_Finishing_Level': row[7],
            'NCBI_Submission_Status': row[8],
            'NCBI Project ID': row[9],
            'Genbank ID': row[10],
            'Gene Count': row[11],
            'IMG': row[12],
            'HOMD ID': row[13],
            'Sequencing Center': row[14],
            'Funding Source': row[15],
            'Strain Repository ID': row[16]

        }

        counter += 1
        first_insrt = human.insert_one(first_five_fields)
        print(first_insrt.inserted_id)

        second_insert = project.insert_one(remaining_fields)
        print(second_insert.inserted_id)

print("Done")