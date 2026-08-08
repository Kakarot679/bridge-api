
from datetime import datetime
from pydantic import BaseModel,ConfigDict

class OrganizationCreate(BaseModel):
    name:str
    slug:str


class OrganizationUpdate(BaseModel):
    name:str|None=None
    slug:str|None=None


class  OrganizationResponse(BaseModel):
    id:int
    name:str
    slug:str
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)
