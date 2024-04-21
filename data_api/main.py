import json
from bson import ObjectId  
from pymongo import MongoClient
from fastapi import FastAPI


def import_json_to_mongodb(json_file, collection_name):
    client = MongoClient('mongodb+srv://gulmaliyevismayil11:gulmaliyevismayil11@classified.lfhzaj0.mongodb.net/?retryWrites=true&w=majority&appName=Classified')
    db = client['Cars_data']
    collection = db[collection_name]

    with open(json_file, 'r') as file:
        data = json.load(file)


    for item in data:
        if '_id' in item:
            item['_id'] = ObjectId(item['_id'])

    collection.insert_many(data)


import_json_to_mongodb('./car-list.json', 'cars_collection')


app = FastAPI()



client = MongoClient('mongodb+srv://gulmaliyevismayil11:gulmaliyevismayil11@classified.lfhzaj0.mongodb.net/?retryWrites=true&w=majority&appName=Classified')
db = client['Cars_data']
collection = db['cars_collection']


@app.get("/cars")
async def get_cars():
  
    cars = list(collection.find())
 
    formatted_cars = []
    for car in cars:
        formatted_car = {
            "brand": car["brand"],
            "models": car["models"]
        }
        formatted_cars.append(formatted_car)
        
    return formatted_cars






