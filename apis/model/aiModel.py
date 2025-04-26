from pydantic import BaseModel
from typing import Optional


class userInputParam(BaseModel):
    prompt: str
    max_length: Optional[int] = 50


class aiRespose(BaseModel):
    response: str
    action: str