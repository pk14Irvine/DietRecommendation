import json
import pandas as pd
from routes.diets import compose_diet_object, insert_into_db

def seed_dietrec():
    filename = "data/diet_recommendations_dataset.csv"
    data = pd.read_csv(filename)
    # data.drop(columns=['Patient_ID'], inplace = True)
    # data.insert(loc = 0, column='id', value=range(1, len(data) + 1))
    data = data.drop_duplicates()
    for _, row in data.iterrows():
        # print("this is row: ", row)
        # print(" ")
        stats = compose_diet_object(row)
        insert_into_db(stats)

    