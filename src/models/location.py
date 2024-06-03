"""Data models for location"""
from pydantic import BaseModel

class Location(BaseModel):
    latitude: float
    longitude: float
    confidence: float
# Modified 2025-09-23
# Modified 2023-12-01
# Modified 2024-06-03
