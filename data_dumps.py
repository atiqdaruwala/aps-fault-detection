import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ =="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print (f"Rows and Columns: {df.shape}")

    #converting to json so that we can dump this into mongodb
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())


    #insert converted json records in mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

