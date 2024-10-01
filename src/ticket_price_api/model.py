"""FastAPI router module."""

import mlflow.pyfunc
from dotenv import load_dotenv
import os
import pandas as pd
from .schemas import Flight, PricePrediction


load_dotenv()
remote_server_uri = os.getenv("MLFLOW_TRACKING_URI")
mlflow.set_tracking_uri(remote_server_uri)

model_name = "plane_price_catboost"
model = mlflow.pyfunc.load_model(f"models:/{model_name}/production")

coords = pd.read_csv(os.path.join(os.path.dirname(__file__), "./airport_coords.csv"))


def predict(flights: list[Flight]) -> list[PricePrediction]:
    df = pd.DataFrame.from_dict([f.model_dump() for f in flights])
    df["travelDuration"] = df["travelDuration"].astype(int)

    airport_columns = ["startingAirport", "destinationAirport"]
    for col in airport_columns:
        df = df.set_index(col).join(coords, rsuffix=f"_{col}").reset_index()

    pred = model.predict(df)

    return [
        PricePrediction(flight=flight, price=price)
        for flight, price in zip(flights, pred)
    ]
