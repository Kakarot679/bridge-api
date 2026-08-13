
from pydantic import BaseModel,ConfigDict
from datetime import datetime
from app.models.enums import ConnectionStatus


class ConnectionCreate(BaseModel):
    organization_id:int
    provider_id:int
    access_token:str
    refresh_token:str|None=None




class ConnectionUpdate(BaseModel):
    status:ConnectionStatus|None=None
    access_token:str|None=None
    refresh_token:str|None=None




class ConnectionResponse(BaseModel):
    id:int
    organization_id:int
    provider_id:int
    status:ConnectionStatus
    created_at:datetime
    updated_at:datetime
    expires_at:datetime|None

    model_config=ConfigDict(from_attributes=True)



