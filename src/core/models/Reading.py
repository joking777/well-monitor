
from pydantic import BaseModel

class Reading(BaseModel):
    timestamp: str
    depth: float
    temperature: float
    barometer: float
        