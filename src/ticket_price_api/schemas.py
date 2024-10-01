"""Request / response schemas for ticket price app."""

from pydantic import BaseModel


class Flight(BaseModel):
    """Flight data for prediction"""

    destinationAirport: str
    startingAirport: str
    travelDuration: float
    elapsedDays: int
    day_of_week: int
    month: int
    stops: int


class PricePrediction(BaseModel):
    """Price prediction for a flight"""

    flight: Flight
    price: float
