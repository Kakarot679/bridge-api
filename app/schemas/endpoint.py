from pydantic import BaseModel,ConfigDict
from app.models.enums import HttpMethod
from datetime import datetime

class EndpointCreate(BaseModel):
  name:str
  provider_id:int
  method:HttpMethod
  path:str
  description:str|None=None

class EndpointUpdate(BaseModel):
  name:str|None=None
  method:HttpMethod|None=None
  path:str|None=None
  description:str|None=None


class EndpointResponse(BaseModel):
  id:int
  name:str
  provider_id:int
  method:HttpMethod
  path:str
  description:str|None
  created_at:datetime

  model_config=ConfigDict(from_attributes=True)

