from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.provider import ProviderCreate,ProviderUpdate
from app.models.provider import Provider
from fastapi import HTTPException,status
from sqlalchemy.exc import IntegrityError


class ProviderService:
    
    def __init__(self,db:Session):
        self.db= db

    def create_provider(self,provider_data:ProviderCreate):
       """Create a new provider."""

       provider=Provider(**provider_data.model_dump())

       self.db.add(provider)
       try:
          self.db.commit()
       except IntegrityError:
          self.db.rollback()
          raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Provider violates a unique constraint."
        )
       self.db.refresh(provider)

       return provider

    def get_provider(self,provider_id:int):
        """Return a provider by its ID."""
        # statement=self.db.query(Provider).filter(Provider.id==provider_id).first()
        statement=select(Provider).where(Provider.id==provider_id)
        result=self.db.execute(statement)
        provider=result.scalar_one_or_none()
        if provider is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="provider not found"
            )
        return provider

    def list_providers(self):
        """Return all providers."""
        statement=select(Provider)
        result=self.db.execute(statement)
        return result.scalars().all()


    def update_provider(self,provider_id:int,provider_data:ProviderUpdate):
        """updates the  provider."""
        provider=self.get_provider(provider_id)

        update_data=provider_data.model_dump(exclude_unset=True)

        for field,value in update_data.items():
            setattr(provider,field,value)



        try:
              self.db.commit()
        except IntegrityError:
              self.db.rollback()
              raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Provider violates a unique constraint."
            )
        self.db.refresh(provider)

        return provider

    def delete_provider(self,provider_id:int):
        """Deletes the provider."""
        provider=self.get_provider(provider_id)

        self.db.delete(provider)
        self.db.commit()

        




        


       
       
       