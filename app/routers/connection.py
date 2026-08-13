from fastapi import APIRouter,Depends,HTTPException,status
from app.schemas.connection import ConnectionResponse,ConnectionCreate,ConnectionUpdate
from app.services.connection_service import ConnectionService
from sqlalchemy.orm import Session
from app.db.session import get_db



router=APIRouter(
    prefix="/connections",
    tags=["Connections"]
)


@router.post("/",response_model=ConnectionResponse,status_code=status.HTTP_201_CREATED)
def create_connection(connection_data:ConnectionCreate,db:Session=Depends(get_db)):
    service=ConnectionService(db)
    create=service.create_connection(connection_data)
    return create

@router.get("/{connection_id}",response_model=ConnectionResponse)
def get_connection(connection_id:int,db:Session=Depends(get_db)):
    service=ConnectionService(db)
    result=service.get_connection(connection_id)
    return result

@router.get("/",response_model=list[ConnectionResponse])
def get_connections(db:Session=Depends(get_db)):
    service=ConnectionService(db)
    result=service.get_connections()
    return result



@router.patch("/{connection_id}",response_model=ConnectionResponse)
def update_connection(connection_id:int,connection_data:ConnectionUpdate,db:Session=Depends(get_db)):
    service=ConnectionService(db)
    update=service.update_connection(connection_id,connection_data)
    return update


@router.delete("/{connection_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_connection(connection_id:int,db:Session=Depends(get_db)):
    service=ConnectionService(db)
    service.delete_connection(connection_id)
    return




