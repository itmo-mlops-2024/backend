"""FastAPI router module."""

from fastapi import FastAPI
from . import schemas, model
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.post("/predict", response_model=list[schemas.PricePrediction])
async def get_matching_jobs(flights: list[schemas.Flight]):
    return model.predict(flights)
