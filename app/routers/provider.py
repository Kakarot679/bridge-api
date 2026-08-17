from app.services.provider_service import ProviderService
from app.schemas.provider import ProviderUpdate,ProviderCreate,ProviderResponse
from app.db.session import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi import status
from app.core.deps import get_current_user
from app.models.user import User


router=APIRouter(
    prefix="/providers",
    tags=["Providers"] )


def get_provider_service(db: Session = Depends(get_db)) -> ProviderService:
    return ProviderService(db)


@router.post("/",response_model=ProviderResponse,status_code=status.HTTP_201_CREATED)
def create_provider(provider_data: ProviderCreate,service:ProviderService=Depends(get_provider_service),current_user:User=Depends(get_current_user)):
    provider=service.create_provider(provider_data)
    return provider

@router.get("/",response_model=list[ProviderResponse])
def get_providers(service:ProviderService=Depends(get_provider_service),current_user:User=Depends(get_current_user)):
    provider=service.list_providers()
    return provider


@router.get("/{provider_id}",response_model=ProviderResponse)
def get_provider(provider_id:int,service:ProviderService=Depends(get_provider_service),current_user:User=Depends(get_current_user)):
      provider=service.get_provider(provider_id)
      return provider


@router.patch("/{provider_id}",response_model=ProviderResponse)
def update_provider(provider_id:int,provider_data:ProviderUpdate,service:ProviderService=Depends(get_provider_service),current_user:User=Depends(get_current_user)):
     result=service.update_provider(provider_id,provider_data)
     return result


@router.delete("/{provider_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_provider(provider_id:int,service:ProviderService=Depends(get_provider_service),current_user:User=Depends(get_current_user)):
     result=service.delete_provider(provider_id)
     return
    
