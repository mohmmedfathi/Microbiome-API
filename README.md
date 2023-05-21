# microbiome API

[![LinkedIn][linkedin-shield]][linkedin-url]
[![MIT License][license-shield]][license-url]

<div>

<h3 align="center"> Human microbiome API</h3>

  <p align="center">
      
    
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
  API is implemented with django and mongodb to make various operations on Human Microbiome Dataset. </br>
  
  **Project Goals :** </br>
  * **Data Accessibility** : provide a standardized and easily accessible interface for researchers, scientists, and other stakeholders to interact with the Human Microbiome Data. They can access the data remotely, integrate it into their own workflows,without needing to understand the underlying data storage or processing mechanisms.
  * **Advanced Querying and Analysis** : Researchers can perform complex queries to extract specific subsets of data based on various criteria, such as body sites, sequencing methods, or disease statuses using one API endpoint.
  * **Documentation and Standardization** : provide comprehensive documentation and standardization for the Human Microbiome Data. includes describing the data structure,explaining the API endpoints and usage.
  </br>
  
  **but why MongoDB not SQL(Postgres,MySQL,....) :** </br>
  * **Scalability** : MongoDB is a NoSQL database that suitable for handling large volumes of data. The Human Microbiome Data dataset is extensive, involving samples from 18 different body sites and potentially thousands of individuals. 
  * **Flexibility** : The Human Microbiome Data encompasses various data types, such as 16S bacterial marker gene sequencing, whole metagenome shotgun sequencing, and whole genome sequencing. With MongoDB, we can store and retrieve these diverse data types without the need for extensive schema modifications.
  * **Querying and Aggregation** : MongoDB provides a powerful querying and aggregation framework, which is particularly advantageous when working with large datasets so we can perform complex queries and aggregations on the Human Microbiome Data to extract specific information or derive meaningful insights. 
    
<br>


## Built With
* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

## Getting started
* Python <= 3.10.6
* Pip <= 22.0.2
* Python virtual environment

1. Clone the repo
   ```sh
   git clone https://github.com/mohmmedfathi/micro_test && cd micro_test
   ```
2. Create virtual environment
   ```sh
   python3 -m venv venv
   ```
3. Activate virtual environment
   ```sh
   source venv/bin/activate
   ```
4. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Migrate models
   ```sh
   python manage.py migrate
   ```
6. Run server
   ```sh
   python manage.py runserver 
   ```
### Project Layout 


```tree
├── microbiome
|   ├── settings.py
|   ├── urls.py
|
├── human_info
|   ├── urls.py
│   ├── views.py
│   ├── pymongo.py
|
│── project_info
|   ├── urls.py
|   ├── views.py
│   ├── pymongo.py
|
|── disease_info
|   ├── urls.py
|   ├── views.py
│   ├── pymongo.py

```

### A brief description project:
the project is consist of 3 apps (each one of them represent collection in MongoDB) :
* human_info <make endpoint as link>
json attribute : 
  - json crack
  - field explaination kaggle

* project_info
json attribute : 

* disease_info
json attribute : 


### human_info app endpoints

  **endpoints of human**
  
### project_info app endpoints
  
#### 1 - list all project_info data 
```
    GET /project_info/list/
```
sample output : 
```json
[
  {
    "_id": {
      "$oid": "646511d204a42e20e5795a0b"
    },
    "Human_id": 0,
    "Project_Status": "Complete",
    "NCBI Current_Finishing_Level": "Level 3: Improved-High-Quality Draft",
    "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
    "NCBI Project ID": "33011",
    "Genbank ID": "ACIN00000000",
    "Gene Count": "1950",
    "IMG": "643886181",
    "HOMD ID": "HOMD: tax_389",
    "Sequencing Center": "Washington University Genome Sequencing Center",
    "Funding Source": "NIH-HMP Jumpstart Supplement",
    "Strain Repository ID": "ATCC 49176, CIP 103242"
  },

  {
    "_id": {
      "$oid": "646511db04a42e20e5795a1c"
    },
    "Human_id": 17,
    "Project_Status": "Complete",
    "NCBI Current_Finishing_Level": "Level 2: High-Quality Draft",
    "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
    "NCBI Project ID": "52977",
    "Genbank ID": "AEVG00000000",
    "Gene Count": "2475",
    "IMG": "649989900",
    "HOMD ID": "",
    "Sequencing Center": "Baylor College of Medicine",
    "Funding Source": "NIH-HMP Jumpstart Supplement",
    "Strain Repository ID": "ATCC 25976, NCTC 10219"
  },
  {
    "_id": {
      "$oid": "646511dc04a42e20e5795a1d"
    },
    "Human_id": 18,
    "Project_Status": "Complete",
    "NCBI Current_Finishing_Level": "Level 2: High-Quality Draft",
    "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
    "NCBI Project ID": "173932",
    "Genbank ID": "AWSB00000000",
    "Gene Count": "2320",
    "IMG": "0",
    "HOMD ID": "",
    "Sequencing Center": "Washington University Genome Sequencing Center",
    "Funding Source": "NIH-HMP Sequencing Center",
    "Strain Repository ID": "BEI HM-1065"
  }
  ]
```
  
  <hr>
  
#### 2 - show specific record 
```bash
    GET /project_info/Human_id
    
```
note : **Human_id is Integer**
sample output : 
```json
{
    "_id": {
        "$oid": "646511d204a42e20e5795a0c"
    },
    "Human_id": 1,
    "Project_Status": "Complete",
    "NCBI Current_Finishing_Level": "Level 2: High-Quality Draft",
    "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
    "NCBI Project ID": "46343",
    "Genbank ID": "ADMS00000000",
    "Gene Count": "5755",
    "IMG": "647000200",
    "HOMD ID": "",
    "Sequencing Center": "Baylor College of Medicine",
    "Funding Source": "NIH-HMP Jumpstart Supplement",
    "Strain Repository ID": "ATCC 43553, CIP 55774, LMG 6100"
}
```
 
  <hr>
  
#### 3 - Create one project_info 
``` 
POST /project_info/create_one/
```
sample input : 
```json
{
  "Human_id": 1111,
  "Project_Status": "inprogress",
  "NCBI Current_Finishing_Level": "Level 2",
  "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
  "NCBI Project ID": "38761",
  "Genbank ID": "ACRN00000000",
  "Gene Count": "1853",
  "IMG": "2513237375",
  "HOMD ID": "",
  "Sequencing Center": "Broad Institute",
  "Funding Source": "NIH-HMP Jumpstart Supplement",
  "Strain Repository ID": "BEI HM-236"
}
```
note : **Human_id is unique**

sample output : 
```json
{
    "message": "project_info added",
    "project_info_id": "6465700e1be9f8a7d146e228"
}
```
 
  <hr>
  
#### 4 - Create bulk project_info 
``` 
POST /project_info/create_many/
```
sample input : 
```json
[
    {
  "Human_id": 1112,
  "Project_Status": "complte",
  "NCBI Current_Finishing_Level": "Level 90",
  "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
  "NCBI Project ID": "38761",
  "Genbank ID": "ACRN00000000",
  "Gene Count": "1853",
  "IMG": "2513237375",
  "HOMD ID": "",
  "Sequencing Center": "Broad Institute",
  "Funding Source": "NIH-HMP Jumpstart Supplement",
  "Strain Repository ID": "BEI HM-236"
},
    {
  "Human_id": 1113,
  "Project_Status": "inprogress",
  "NCBI Current_Finishing_Level": "Level 1",
  "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
  "NCBI Project ID": "38761",
  "Genbank ID": "ACRN00000000",
  "Gene Count": "1853",
  "IMG": "2513237375",
  "HOMD ID": "",
  "Sequencing Center": "Broad Institute",
  "Funding Source": "NIH-HMP Jumpstart Supplement",
  "Strain Repository ID": "BEI HM-236"
}
]

```
note : **Human_id is unique**
  
sample output : 
```json
{
    "message": "2 documents inserted"
}
``` 
  <hr>
  
#### 5 - MongoDB aggregatation Endpoint
  
**Aggregate all project_info objects with optional filtering by domain, sorting, and grouping.** <br>

**Query parameters:**
  * domain: filter by domain (optional)
  * sort_by: sort by field (optional) 
  * group_by: group by field (optional)
           
#### how to use the endpoit : 
  
![carbon](https://github.com/mohmmedfathi/microtest/assets/64088888/eb2fc13e-dc86-42b4-9488-b3f08991ca0f)
  <br>

 **example :** 
  
```
 GET  /project_info/aggregate_project_info?
  Project_Status=Complete&
  sort_by=31019&
  group_by=Gene Count
```  
sample output :
  
  ![carbon](https://github.com/mohmmedfathi/microtest/assets/64088888/a35e6ec6-ec0d-4c13-8c27-75ffe817efc0)
  
<br>
  
```json
  [
  {
    "data": {
      "_id": {
        "$oid": "646511d204a42e20e5795a0b"
      },
      "Human_id": 0,
      "Project_Status": "Complete",
      "NCBI Current_Finishing_Level": "Level 3: Improved-High-Quality Draft",
      "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
      "NCBI Project ID": "33011",
      "Genbank ID": "ACIN00000000",
      "Gene Count": "1950",
      "IMG": "643886181",
      "HOMD ID": "HOMD: tax_389",
      "Sequencing Center": "Washington University Genome Sequencing Center",
      "Funding Source": "NIH-HMP Jumpstart Supplement",
      "Strain Repository ID": "ATCC 49176, CIP 103242"
    }
  },
  {
    "data": {
      "_id": {
        "$oid": "646511d204a42e20e5795a0c"
      },
      "Human_id": 1,
      "Project_Status": "Complete",
      "NCBI Current_Finishing_Level": "Level 2: High-Quality Draft",
      "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
      "NCBI Project ID": "46343",
      "Genbank ID": "ADMS00000000",
      "Gene Count": "5755",
      "IMG": "647000200",
      "HOMD ID": "",
      "Sequencing Center": "Baylor College of Medicine",
      "Funding Source": "NIH-HMP Jumpstart Supplement",
      "Strain Repository ID": "ATCC 43553, CIP 55774, LMG 6100"
    }
  },
  {
    "data": {
      "_id": {
        "$oid": "646511d304a42e20e5795a0d"
      },
      "Human_id": 2,
      "Project_Status": "Complete",
      "NCBI Current_Finishing_Level": "Level 5: Non-contiguous Finished",
      "NCBI_Submission_Status": "6. annotation (and sequence) public on NCBI site",
      "NCBI Project ID": "38739",
      "Genbank ID": "ACRC00000000",
      "Gene Count": "6010",
      "IMG": "0",
      "HOMD ID": "HOMD: tax_343",
      "Sequencing Center": "Broad Institute",
      "Funding Source": "NIH-HMP Jumpstart Supplement",
      "Strain Repository ID": "BEI HM-235"
    }
  }
]
```
   
  <hr>
  
#### 6 - create MongoDB index 
  
![carbon (1)](https://github.com/mohmmedfathi/microtest/assets/64088888/110404bd-4451-400f-9736-07df7e1f211d)

 example : 
  
```
    POST /project_info/create_index?field=Gene Count&order=1
```
  
sample output : 
  
```
Index created on field "Gene Count" with name "Gene Count_1" 
 current indexes = "{'_id_': {'v': 2, 'key': [('_id', 1)]}, 'Gene Count_1': {'v': 2, 'key': [('Gene Count', 1)]}}"
```
  
  <hr>
   
 
#### 7 - show all indexes 
```
    GET /project_info/show_indexes/
```
  
sample output : 
  
```json
{
    "_id_": {
        "v": 2,
        "key": [
            [
                "_id",
                1
            ]
        ]
    },
    "Gene Count_1": {
        "v": 2,
        "key": [
            [
                "Gene Count",
                1
            ]
        ]
    }
}
```
### disease_info app endpoints
  

#### 1 - list all disease_info data 
```
    GET /disease_info/list/
```
sample output : 
```json
[
  {
    "_id": 1,
    "﻿disease": "MED.DISEASES.Blood.Anemia",
    "MED.DISEASES.Blood.Anemia": "1",
    "MED.DISEASES.Blood.Thrombosis": "0.030155518",
    "MED.DISEASES.Cancer.Any": "0.023660698",
    "MED.DISEASES.Cardiovascular.Arrythmia.MedDiagnosed": "0.034828556",
    "MED.DISEASES.Cardiovascular.Colesterol.high": "-0.013506254",
    "MED.DISEASES.Cardiovascular.Heart.Attack": "-0.026579618",
    "MED.DISEASES.Cardiovascular.Heart.Failure.Disorder": "-0.005956634",
    "MED.DISEASES.Cardiovascular.Heartrate.complains": "0.092097199",
    "MED.DISEASES.Cardiovascular.Hypertension": "0.032507649",
    "MED.DISEASES.Endocrine.DiabetesT2": "0.001839968",
    "MED.DISEASES.Gastrointestinal.Stomach.Ulcer": "0.024063959",
    "MED.DISEASES.Hepatologic.Gallstones": "0.064607811",
    "MED.DISEASES.Mental.Any": "0.109039221",
    "MED.DISEASES.Mental.Burn.Out": "0.039675773",
    "MED.DISEASES.Mental.Depression": "0.048660138",
    "MED.DISEASES.Mental.Other.anxiety": "0.051273785",
    "MED.DISEASES.Mental.Panic.disorder": "0.054330785",
    "MED.DISEASES.Neurological.Dizziness.Falling": "0.013315382",
    "MED.DISEASES.Neurological.Mental.Fibromyalgia": "0.068923906",
    "MED.DISEASES.Neurological.Migraine": "0.138918931",
    "MED.DISEASES.Other.Autoimmune.Rheumatoid.Artritis": "0.033217646",
    "MED.DISEASES.Skin.Autoimmune.Atopic.dermatitis": "0.103226315",
    "MED.DISEASES.Skin.Autoimmune.Psoriasis": "0.009517194",
    "MED.DISEASES.Skin.Autoimmune.Severe.acne": "0.060007583",
    "MED.DISEASES.Gastrointestinal.Rome3_IBS.Any": "0.04954944",
    "MED.DISEASES.None.No.Diseases": "-0.220571981"
  },
  {
    "_id": 2,
    "﻿disease": "MED.DISEASES.Blood.Thrombosis",
    "MED.DISEASES.Blood.Anemia": "0.131026313",
    "MED.DISEASES.Blood.Thrombosis": "1",
    "MED.DISEASES.Cancer.Any": "0.023773871",
    "MED.DISEASES.Cardiovascular.Arrythmia.MedDiagnosed": "0.03904039",
    "MED.DISEASES.Cardiovascular.Colesterol.high": "0.04208665",
    "MED.DISEASES.Cardiovascular.Heart.Attack": "-0.013205939",
    "MED.DISEASES.Cardiovascular.Heart.Failure.Disorder": "-0.005303241",
    "MED.DISEASES.Cardiovascular.Heartrate.complains": "0.030620218",
    "MED.DISEASES.Cardiovascular.Hypertension": "0.03232672",
    "MED.DISEASES.Endocrine.DiabetesT2": "0.019818901",
    "MED.DISEASES.Gastrointestinal.Stomach.Ulcer": "0.006462143",
    "MED.DISEASES.Hepatologic.Gallstones": "0.039995356",
    "MED.DISEASES.Mental.Any": "0.007361899",
    "MED.DISEASES.Mental.Burn.Out": "0.012085357",
    "MED.DISEASES.Mental.Depression": "-0.00757754",
    "MED.DISEASES.Other.Osteoarthritis": "0.035991451",
    "MED.DISEASES.Other.Osteoporosis": "0.031793733",
    "MED.DISEASES.Other.RSI": "0.017164426",
    "MED.DISEASES.Pulmonary.Autoimmune.Asthma": "0.000583128",
    "MED.DISEASES.Pulmonary.COPD": "0.022380562",
    "MED.DISEASES.Skin.Autoimmune.Atopic.dermatitis": "0.001593836",
    "MED.DISEASES.Skin.Autoimmune.Psoriasis": "-0.005318063",
    "MED.DISEASES.Skin.Autoimmune.Severe.acne": "0.002060624",
    "MED.DISEASES.Gastrointestinal.Rome3_IBS.Any": "0.01101488",
    "MED.DISEASES.None.No.Diseases": "-0.080449008"
  }
  ]
```
  
  <hr> 
  
#### 2 - show specific record 
```bash
    GET /disease_info/disease_id
    
```
note : **disease_id is Integer**
sample output : 
```json
{
  "_id": 1,
  "﻿disease": "MED.DISEASES.Blood.Anemia",
  "MED.DISEASES.Blood.Anemia": "1",
  "MED.DISEASES.Blood.Thrombosis": "0.030155518",
  "MED.DISEASES.Cancer.Any": "0.023660698",
  "MED.DISEASES.Cardiovascular.Arrythmia.MedDiagnosed": "0.034828556",
  "MED.DISEASES.Cardiovascular.Colesterol.high": "-0.013506254",
  "MED.DISEASES.Cardiovascular.Heart.Attack": "-0.026579618",
  "MED.DISEASES.Cardiovascular.Heart.Failure.Disorder": "-0.005956634",
  "MED.DISEASES.Cardiovascular.Heartrate.complains": "0.092097199",
  "MED.DISEASES.Cardiovascular.Hypertension": "0.032507649",
  "MED.DISEASES.Endocrine.DiabetesT2": "0.001839968",
  "MED.DISEASES.Gastrointestinal.Stomach.Ulcer": "0.024063959",
  "MED.DISEASES.Hepatologic.Gallstones": "0.064607811",
  "MED.DISEASES.Mental.Any": "0.109039221"
}
```
 
  <hr>
  
#### 3 - Create one disease_info 
``` 
POST /disease_info/create_one/
```
sample input : 
```json
{
  "_id": 100,
  "﻿disease": "MED.DISEASES.Autism",
  "MED.DISEASES.Blood.Anemia": "2",
  "MED.DISEASES.Blood.Thrombosis": "0",
  "MED.DISEASES.Cancer.Any": "0",
  "MED.DISEASES.Cardiovascular.Arrythmia.MedDiagnosed": "0.034828556",
  "MED.DISEASES.Cardiovascular.Colesterol.high": "-0.013506254",
  "MED.DISEASES.Cardiovascular.Heart.Attack": "-0.026579618",
  "MED.DISEASES.Cardiovascular.Heart.Failure.Disorder": "-0.005956634",
  "MED.DISEASES.Cardiovascular.Heartrate.complains": "0.092097199",
  "MED.DISEASES.Cardiovascular.Hypertension": "0.032507649",
  "MED.DISEASES.Endocrine.DiabetesT2": "0.001839968",
  "MED.DISEASES.Gastrointestinal.Stomach.Ulcer": "0.024063959",
  "MED.DISEASES.Hepatologic.Gallstones": "0.064607811",
  "MED.DISEASES.Mental.Any": "0.109039221",
  "MED.DISEASES.Mental.Burn.Out": "0.039675773",
  "MED.DISEASES.Mental.Depression": "0.048660138",
  "MED.DISEASES.Mental.Other.anxiety": "0.051273785",
  "MED.DISEASES.Mental.Panic.disorder": "0.054330785",
  "MED.DISEASES.Neurological.Dizziness.Falling": "0.013315382",
  "MED.DISEASES.Neurological.Mental.Fibromyalgia": "0.068923906",
  "MED.DISEASES.Neurological.Migraine": "0.138918931",
  "MED.DISEASES.Other.Autoimmune.Rheumatoid.Artritis": "0.033217646",
  "MED.DISEASES.Other.Chronic.cystitis": "0.086287333",
  "MED.DISEASES.Other.Chronic.Inflammation.Throatnose": "0.051093201",
  "MED.DISEASES.Other.Chronic.Muscle.Weakness": "0.070110742",
  "MED.DISEASES.Other.Fractures.Other": "0.000555412",
  "MED.DISEASES.Other.Incontinence": "0.067330315",
  "MED.DISEASES.Other.Kidney.Stones": "-0.011400175",
  "MED.DISEASES.Other.Osteoarthritis": "0.055869733",
  "MED.DISEASES.Other.Osteoporosis": "0.039045686",
  "MED.DISEASES.Other.RSI": "0.011864857",
  "MED.DISEASES.Pulmonary.Autoimmune.Asthma": "0.019167002",
  "MED.DISEASES.Pulmonary.COPD": "0.009635455",
  "MED.DISEASES.Skin.Autoimmune.Atopic.dermatitis": "0.103226315",
  "MED.DISEASES.Skin.Autoimmune.Psoriasis": "0.009517194",
  "MED.DISEASES.Skin.Autoimmune.Severe.acne": "0.060007583",
  "MED.DISEASES.Gastrointestinal.Rome3_IBS.Any": "0.04954944",
  "MED.DISEASES.None.No.Diseases": "-0.220571981"
}
```
note : **Human_id is unique**

sample output : 
```json
{
    "message": "disease_info added",
    "disease_info_id": "100"
}
```
 
  <hr>
  
#### 4 - Create bulk disease_info 
``` 
POST /disease_info/create_many/
```
sample input : 
```json
[
  {
    "_id": 101,
    "﻿disease": "MED.DISEASES.cancer",
    "MED.DISEASES.Blood.Anemia": "0",
    "MED.DISEASES.Blood.Thrombosis": "0",
    "MED.DISEASES.Cancer.Any": "0",
    "MED.DISEASES.Cardiovascular.Arrythmia.MedDiagnosed": "0.034828556",
    "MED.DISEASES.Cardiovascular.Colesterol.high": "-0.013506254",
    "MED.DISEASES.Cardiovascular.Heart.Attack": "-0.026579618",
    "MED.DISEASES.Cardiovascular.Heart.Failure.Disorder": "-0.005956634",
    "MED.DISEASES.Cardiovascular.Heartrate.complains": "0.092097199",
    "MED.DISEASES.Cardiovascular.Hypertension": "0.032507649",
    "MED.DISEASES.Endocrine.DiabetesT2": "0.001839968",
    "MED.DISEASES.Gastrointestinal.Stomach.Ulcer": "0.024063959",
    "MED.DISEASES.Hepatologic.Gallstones": "0.064607811",
    "MED.DISEASES.Mental.Any": "0.109039221",
    "MED.DISEASES.Mental.Burn.Out": "0.039675773",
    "MED.DISEASES.Mental.Depression": "0.048660138",
    "MED.DISEASES.Mental.Other.anxiety": "0.051273785"
  },
  {
    "_id": 102,
    "﻿disease": "MED.DISEASES.Autism",
    "MED.DISEASES.Blood.Anemia": "2",
    "MED.DISEASES.Blood.Thrombosis": "0",
    "MED.DISEASES.Cancer.Any": "0",
    "MED.DISEASES.Cardiovascular.Arrythmia.MedDiagnosed": "0.034828556",
    "MED.DISEASES.Cardiovascular.Colesterol.high": "-0.013506254",
    "MED.DISEASES.Cardiovascular.Heart.Attack": "-0.026579618",
    "MED.DISEASES.Cardiovascular.Heart.Failure.Disorder": "-0.005956634",
    "MED.DISEASES.Cardiovascular.Heartrate.complains": "0.092097199",
    "MED.DISEASES.Cardiovascular.Hypertension": "0.032507649",
    "MED.DISEASES.Endocrine.DiabetesT2": "0.001839968",
    "MED.DISEASES.Gastrointestinal.Stomach.Ulcer": "0.024063959",
    "MED.DISEASES.Hepatologic.Gallstones": "0.064607811",
    "MED.DISEASES.Mental.Any": "0.109039221",
    "MED.DISEASES.Mental.Burn.Out": "0.039675773",
    "MED.DISEASES.Mental.Depression": "0.048660138",
    "MED.DISEASES.Mental.Other.anxiety": "0.051273785",
    "MED.DISEASES.Mental.Panic.disorder": "0.054330785",
    "MED.DISEASES.Neurological.Dizziness.Falling": "0.013315382",
    "MED.DISEASES.Neurological.Mental.Fibromyalgia": "0.068923906"   
  }
]
```
note : **disease_id is unique**

sample output : 
```json
{
    "message": "2 documents inserted"
}
``` 
  <hr>
  
#### 6 - create MongoDB index 
  
![carbon (1)](https://github.com/mohmmedfathi/microtest/assets/64088888/110404bd-4451-400f-9736-07df7e1f211d)

 example : 
  
```
    GET /disease_info/create_index?field=MED.DISEASES.Cardiovascular.Colesterol.high&order=-1/
```
  
sample output : 
  
```
  Index created on field "_id" with name "_id_1" 
 current indexes = "{'_id_': {'v': 2, 'key': [('_id', 1)]}}"
```
  
  <hr>
   
 
#### 7 - show all indexes 
```
    GET /disease_info/show_indexes/
```
  
sample output : 
  
```json
{
    "_id_": {
        "v": 2,
        "key": [
            [
                "_id",
                1
            ]
        ]
    },
    "MED.DISEASES.Cardiovascular.Colesterol.high_-1": {
        "v": 2,
        "key": [
            [
                "MED.DISEASES.Cardiovascular.Colesterol.high",
                -1
            ]
        ]
    }
}
```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mohammed-fathi-4a08071a7/
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://docs.djangoproject.com/en/3.2/
[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://docs.python.org/3/
