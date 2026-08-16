from sqlalchemy.orm import Session
from app.schemas.user import UserCreate,UserResponse
from app.core.security import hash_password,create_access_token
from app.models.user import User
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,status
from app.services.organization_service import OrganizationService
class UserService:
    def __init__(self, db:Session):
        self.db=db


    def register_user(self,user_data:UserCreate):

      service=OrganizationService(self.db)
      organization=service.get_organization(user_data.organization_id)


      hashed_pw=  hash_password(user_data.password)
      data=User(
         name=user_data.name,
         email=user_data.email,
         organization_id=user_data.organization_id,
         hashed_password=hashed_pw
      )
      self.db.add(data)
      try:
         self.db.commit()
      except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists."
            )
      self.db.refresh(data)
      return data



    