
from fastapi import APIRouter,Depends,status
from app.schemas.endpoint import EndpointResponse,EndpointCreate,EndpointUpdate
from app.services.endpoint_service import EndpointService
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.deps import get_current_user
from app.models.user import User





router=APIRouter(prefix="/endpoint"
                   ,tags=["Endpoints"])


def get_endpoint_service(db: Session = Depends(get_db)) -> EndpointService:
    return EndpointService(db)


@router.get("/{endpoint_id}",response_model=EndpointResponse)
def get_endpoint(endpoint_id:int,service:EndpointService=Depends(get_endpoint_service),current_user:User=Depends(get_current_user)):
    endpoint=service.get_endpoint(endpoint_id)
    return endpoint

@router.get("/",response_model=list[EndpointResponse])
def get_endpoints(service:EndpointService=Depends(get_endpoint_service),current_user:User=Depends(get_current_user)):
    endpoints=service.get_endpoints()
    return endpoints

@router.post("/",response_model=EndpointResponse,status_code=status.HTTP_201_CREATED)
def create_endpoint(endpoint_data:EndpointCreate,service:EndpointService=Depends(get_endpoint_service),current_user:User=Depends(get_current_user)):
    endpoint=service.create_endpoint(endpoint_data)
    return endpoint

@router.patch("/{endpoint_id}",response_model=EndpointResponse)
def update_endpoint(endpoint_id:int,endpoint_data:EndpointUpdate,service:EndpointService=Depends(get_endpoint_service),current_user:User=Depends(get_current_user)):
    endpoint=service.update_endpoint(endpoint_id,endpoint_data)
    return endpoint

@router.delete("/{endpoint_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_endpoint(endpoint_id:int,service:EndpointService=Depends(get_endpoint_service),current_user:User=Depends(get_current_user)):
    service.delete_endpoint(endpoint_id)



    





