"""FastAPI router module."""

from fastapi import FastAPI
from . import schemas, model

app = FastAPI()


@app.post("/predict", response_model=list[schemas.PricePrediction])
async def get_matching_jobs(flights: list[schemas.Flight]):
    return model.predict(flights)
