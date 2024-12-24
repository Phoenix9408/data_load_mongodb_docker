from pymongo import MongoClient

## Projet's Input Path

Data_Input_dir = "/data/"
File_name = "healthcare_dataset.csv"


client = MongoClient("mongodb://ocr:ocr@mongo_db:27017/ocr?authSource=admin")



## collection name
Collection = 'Medical'