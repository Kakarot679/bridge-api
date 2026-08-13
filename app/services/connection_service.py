from sqlalchemy.orm import Session
from app.schemas.connection import ConnectionCreate,ConnectionUpdate
from sqlalchemy import select
from app.models.connection import Connection
from  fastapi import status,HTTPException
from sqlalchemy.exc import IntegrityError
from app.services.organization_service import OrganizationService
from app.services.provider_service import ProviderService
from app.models.enums import AuthType
class ConnectionService:
    
    def __init__(self,db:Session):
        self.db=db

    def create_connection(self,connection_data:ConnectionCreate):
        """Create a new connection."""
        organization_service = OrganizationService(self.db)
        organization_service.get_organization(connection_data.organization_id)
        provider_service = ProviderService(self.db)
        provider=provider_service.get_provider(connection_data.provider_id)
        
        if provider.auth_type == AuthType.OAUTH2 and not connection_data.refresh_token:
            raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="refresh_token is required for OAuth2 providers."
        )



        connection=Connection(**connection_data.model_dump())
        self.db.add(connection)
        try:
            self.db.commit()
        except IntegrityError:
            
            self.db.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="connection voilates unique constraint")
        self.db.refresh(connection)
        return connection



    def get_connection(self,connection_id:int):
        """Return a connection by its ID."""
        statement=select(Connection).where(Connection.id==connection_id)
        result=self.db.execute(statement)
        connection=result.scalar_one_or_none()
        if connection is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="connection not found"
            )
        return connection

    def get_connections(self):
        """Return all connections."""
        statement=select(Connection)
        result=self.db.execute(statement)
        return result.scalars().all()

    def update_connection(self,connection_id:int,connection_data:ConnectionUpdate):
        """updates the connection."""
        connection=self.get_connection(connection_id)
        update_data=connection_data.model_dump(exclude_unset=True)

        for field,value in update_data.items():
            setattr(connection,field,value)

        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="connection is hitting voilation constraint"
            )

        self.db.refresh(connection)

        return connection

    def delete_connection(self,connection_id:int):
        """Delete a connection by its ID."""
        connection=self.get_connection(connection_id)
        self.db.delete(connection)
        self.db.commit()
        


        