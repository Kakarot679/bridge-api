from pydantic import BaseModel,ConfigDict
from datetime import datetime

from app.models.enums import AuthType




class ProviderCreate(BaseModel):
    name:str
    slug:str
    base_url:str
    auth_type:AuthType
    token_url:str


class ProviderResponse(BaseModel):

    id:int 
    name:str
    slug:str
    base_url:str
    auth_type:AuthType
    created_at:datetime
    token_url:str
    model_config = ConfigDict(from_attributes=True)
    


class ProviderUpdate(BaseModel):
    name:str|None=None
    slug:str|None=None
    base_url:str|None=None
    auth_type:AuthType|None=None
    token_url:str|None=None

  
