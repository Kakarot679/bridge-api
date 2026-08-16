from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.core.security import verify_password,create_access_token
from fastapi import HTTPException,status
from app.core.config import settings
from datetime import timedelta
class AuthService:
    def __init__(self,db:Session):
        self.db=db

    def authenticate_user(self,email:str,password:str):
        
        statememt=select(User).where(User.email==email)
        result=self.db.execute(statememt)
        user= result.scalars().first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")

        if verify_password(password,user.hashed_password)==False:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")

        access_token=create_access_token(
            data={"sub":str(user.id)},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        )
        return access_token
        
            
        
        


       
                
