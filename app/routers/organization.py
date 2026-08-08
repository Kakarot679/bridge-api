from fastapi import APIRouter,Depends
from app.schemas.organization import OrganizationResponse,OrganizationCreate,OrganizationUpdate
from app.services.organization_service import OrganizationService
from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import status





router=APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)

@router.post("/",response_model=OrganizationResponse,status_code=status.HTTP_201_CREATED)
def create_organization(organization_data:OrganizationCreate,db:Session=Depends(get_db)):
    service=OrganizationService(db)
    organization=service.create_organization(organization_data)
    return organization


@router.get("/{organization_id}",response_model=OrganizationResponse)
def get_organization(organization_id:int ,db:Session=Depends(get_db)):
    service=OrganizationService(db)
    organization=service.get_organization(organization_id)
    return organization

@router.get("/",response_model=list[OrganizationResponse])
def get_organizations(db:Session=Depends(get_db)):
    service=OrganizationService(db)
    organization=service.list_organizations()
    return organization

@router.patch("/{organization_id}",response_model=OrganizationResponse)
def update_organization(organization_id:int,organization_data:OrganizationUpdate,db:Session=Depends(get_db)):
    service=OrganizationService(db)
    organization=service.update_organization(organization_id,organization_data)
    return organization

@router.delete("/{organization_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_organization(organization_id:int,db:Session=Depends(get_db)):
    service=OrganizationService(db)
    service.delete_organization(organization_id)
    return



