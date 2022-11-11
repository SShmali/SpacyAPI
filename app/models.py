from typing import  List, Optional
from pydantic import BaseModel

class RecordDataRequest(BaseModel):
    text: str
    language: str = "en"


class RecordRequest(BaseModel):
    data: RecordDataRequest



class RecordDataResponse(BaseModel):
    entities: List


class Message(BaseModel):
    message: str


class RecordResponse(BaseModel):
    data: RecordDataResponse
    errors: Optional[List[Message]]
    warnings: Optional[List[Message]]

