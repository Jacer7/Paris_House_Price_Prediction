import numpy as np
import pandas as pd
import pickle

from fastapi import FastAPI
from pydantic import BaseModel

from pipeline.preprocess import MODELS_DIR

app = FastAPI()


# Route for test
@app.get("/")
async def index():
    return {"api_name": "linear_regression"}

class Item(BaseModel):
    size: int
    nb_rooms: int
    garden: str
    locations: str  # Est, Sud, Nord, Quest


@app.post("/predict")
async def do_prediction(data: Item):
    encoder = pickle.load(open(MODELS_DIR / 'ohe_encoder.pkl', 'rb'))
    arr1 = encoder.transform([[data.garden, data.locations]]).toarray()
    print(f'Array for test {arr1}')
    rem_arr = [[data.size, data.nb_rooms]]
    # print(rem_arr)
    user_input = np.concatenate((rem_arr, arr1), axis=1)
    # print(user_input)
    model = pickle.load(open(MODELS_DIR /'linearReg.pkl', 'rb'))
    prediction = model.predict(user_input)
    print(prediction[0])
    return (f"Bonjour, The price of your house is predicted to be Euro {prediction[0]} , Merci ! ")


