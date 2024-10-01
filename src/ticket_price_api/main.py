"""FastAPI router module."""

from fastapi import FastAPI

from . import schemas

app = FastAPI()


@app.post("/predict", response_model=list[schemas.PricePrediction])
async def get_matching_jobs(flights: list[schemas.Flight]):
    prediction = [schemas.PricePrediction(flight=flight, price=0) for flight in flights]
    return prediction
