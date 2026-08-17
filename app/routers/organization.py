from fastapi import APIRouter,Depends
from app.schemas.organization import OrganizationResponse,OrganizationCreate,OrganizationUpdate
from app.services.organization_service import OrganizationService
from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import status
from app.core.deps import get_current_user
from app.models.user import User





router=APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)

def get_organization_service(db: Session = Depends(get_db)) -> OrganizationService:
    return OrganizationService(db)


@router.post("/",response_model=OrganizationResponse,status_code=status.HTTP_201_CREATED)
def create_organization(organization_data:OrganizationCreate,service:OrganizationService=Depends(get_organization_service),current_user:User=Depends(get_current_user)):
    organization=service.create_organization(organization_data)
    return organization


@router.get("/{organization_id}",response_model=OrganizationResponse)
def get_organization(organization_id:int ,service:OrganizationService=Depends(get_organization_service),current_user:User=Depends(get_current_user)):
    organization=service.get_organization(organization_id,current_user)
    return organization

@router.get("/",response_model=list[OrganizationResponse])
def get_organizations(service:OrganizationService=Depends(get_organization_service),current_user:User=Depends(get_current_user)):
    organization=service.list_organizations(current_user)
    return organization

@router.patch("/{organization_id}",response_model=OrganizationResponse)
def update_organization(organization_id:int,organization_data:OrganizationUpdate,service:OrganizationService=Depends(get_organization_service),current_user:User=Depends(get_current_user)):
    organization=service.update_organization(organization_id,organization_data,current_user)
    return organization

@router.delete("/{organization_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_organization(organization_id:int,service:OrganizationService=Depends(get_organization_service),current_user:User=Depends(get_current_user)):
    service.delete_organization(organization_id,current_user)
    return



