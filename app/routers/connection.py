from fastapi import APIRouter,Depends,HTTPException,status
from app.schemas.connection import ConnectionResponse,ConnectionCreate,ConnectionUpdate
from app.services.connection_service import ConnectionService
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.deps import get_current_user
from app.models.user import User



router=APIRouter(
    prefix="/connections",
    tags=["Connections"]
)

def get_connection_service(db: Session = Depends(get_db)) -> ConnectionService:
    return ConnectionService(db)

@router.post("/",response_model=ConnectionResponse,status_code=status.HTTP_201_CREATED)
def create_connection(connection_data:ConnectionCreate,service:ConnectionService=Depends(get_connection_service),current_user:User=Depends(get_current_user)):

    return service.create_connection(connection_data,current_user)
    

@router.get("/{connection_id}",response_model=ConnectionResponse)
def get_connection(connection_id:int,service:ConnectionService=Depends(get_connection_service),current_user:User=Depends(get_current_user)):
    return service.get_connection(connection_id,current_user)


@router.get("/",response_model=list[ConnectionResponse])
def get_connections(service:ConnectionService=Depends(get_connection_service),current_user:User=Depends(get_current_user)):
    return service.get_connections(current_user)



@router.patch("/{connection_id}",response_model=ConnectionResponse)
def update_connection(connection_id:int,connection_data:ConnectionUpdate,service:ConnectionService=Depends(get_connection_service),current_user:User=Depends(get_current_user)):
    
    return service.update_connection(connection_id,connection_data,current_user)
    


@router.delete("/{connection_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_connection(connection_id:int,service:ConnectionService=Depends(get_connection_service),current_user:User=Depends(get_current_user)):
    
    return service.delete_connection(connection_id,current_user)
    

@router.post("/{connection_id}/refresh", response_model=ConnectionResponse)
def refresh_connection(connection_id:int,service:ConnectionService=Depends(get_connection_service),current_user:User=Depends(get_current_user)):

    return service.refresh_connection(connection_id,current_user)
  


