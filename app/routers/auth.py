from fastapi import APIRouter,Depends,status
from app.schemas.user import UserCreate,UserResponse
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.auth import Token



router=APIRouter(prefix="/auth",
                 tags=["Auth"])

@router.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def register(user_data:UserCreate,db:Session=Depends(get_db)):
    service=UserService(db)
    user=service.register_user(user_data)
    return user


@router.post("/login",response_model=Token)
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    service=AuthService(db)
    access_token=service.authenticate_user(form_data.username,form_data.password)
    return Token(access_token=access_token,token_type="bearer")
    
  


