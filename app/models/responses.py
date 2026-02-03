from pydantic import BaseModel
from typing import List


class HealthResponse(BaseModel):
    status: str
    message: str


class TelemetryUploadResponse(BaseModel):
    status: str
    samples: int
    channels: List[str]
