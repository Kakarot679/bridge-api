from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    organization_id: int


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    organization_id: int

    model_config = ConfigDict(from_attributes=True)
