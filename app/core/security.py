from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from app.core.config import settings
import jwt

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password:str)  -> str:
    return pwd_context.hash(password)

def verify_password(actual_password:str,hashed_password:str)-> bool:
    return pwd_context.verify(actual_password,hashed_password) 

def create_access_token(data:dict,expires_delta:timedelta):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+expires_delta
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)


def decode_access_token(token:str) -> dict:
    return jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
    