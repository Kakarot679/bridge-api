from app.services.provider_service import ProviderService
from app.schemas.provider import ProviderUpdate,ProviderCreate,ProviderResponse
from app.db.session import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi import status


router=APIRouter(
    prefix="/providers",
    tags=["Providers"] )



@router.post("/",response_model=ProviderResponse,status_code=status.HTTP_201_CREATED)
def create_provider(provider_data: ProviderCreate,db:Session=Depends(get_db)):
    service=ProviderService(db)
    provider=service.create_provider(provider_data)
    return provider

@router.get("/",response_model=list[ProviderResponse])
def get_providers(db:Session=Depends(get_db)):
    service=ProviderService(db)
    provider=service.list_providers()
    return provider


@router.get("/{provider_id}",response_model=ProviderResponse)
def get_provider(provider_id:int,db:Session=Depends(get_db)):
      service=ProviderService(db)
      provider=service.get_provider(provider_id)
      return provider


@router.patch("/{provider_id}",response_model=ProviderResponse)
def update_provider(provider_id:int,provider_data:ProviderUpdate,db:Session=Depends(get_db)):
     service=ProviderService(db)
     result=service.update_provider(provider_id,provider_data)
     return result


@router.delete("/{provider_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_provider(provider_id:int,db:Session=Depends(get_db)):
     service=ProviderService(db)
     result=service.delete_provider(provider_id)
     return 
    
