
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.endpoint import Endpoint
from sqlalchemy import select
from app.schemas.endpoint import EndpointCreate,EndpointResponse,EndpointUpdate
from app.services.provider_service import ProviderService
from sqlalchemy.exc import IntegrityError
class EndpointService:
    def __init__(self,db:Session):
        self.db=db


    def get_endpoint(self,endpoint_id:int):
        statement=select(Endpoint).where(endpoint_id==Endpoint.id)
        result=self.db.execute(statement)
        endpoint=result.scalar_one_or_none()
        if endpoint is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="endpoint not found"
            )
        return endpoint

    def get_endpoints(self):
        statement=select(Endpoint)
        result=self.db.execute(statement)
        return result.scalars().all()

    def create_endpoint(self,endpoint_data:EndpointCreate):
        provider_service=ProviderService(self.db)
        provider=provider_service.get_provider(endpoint_data.provider_id)
        endpoint=Endpoint(**endpoint_data.model_dump())
        self.db.add(endpoint)

        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="endpoint violates unique constraint"
            )
        return endpoint

    def update_endpoint(self,endpoint_id:int,endpoint_data:EndpointUpdate):
        endpoint=self.get_endpoint(endpoint_id)
        update_data=endpoint_data.model_dump(exclude_unset=True)

        for field,value in update_data.items():
            setattr(endpoint,field,value)

        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="endpoint violates unique constraint"
            ) 
        return endpoint


    def delete_endpoint(self,endpoint_id:int):
        endpoint=self.get_endpoint(endpoint_id)
        self.db.delete(endpoint)
        self.db.commit()

  
        



      





        