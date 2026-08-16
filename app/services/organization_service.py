from sqlalchemy.orm import Session
from app.schemas.organization import OrganizationCreate,OrganizationUpdate
from app.models.organization import Organization
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,status
from sqlalchemy import select
from app.models.user import User



class OrganizationService:

    def __init__(self,db:Session):
        self.db= db


    def create_organization(self,organization_data:OrganizationCreate):
        """Create a new organization."""
        organization=Organization(**organization_data.model_dump())
        self.db.add(organization)

        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Organization violates a unique constraint."
            )

        self.db.refresh(organization)
        return organization

    def get_organization(self,organization_id:int,current_user:User|None=None):
        """Return an organization by its ID."""
        statement = select(Organization).where(Organization.id==organization_id)
        result=self.db.execute(statement)
        organization=result.scalar_one_or_none()
        if  organization is None or (current_user is not None and organization.id!=current_user.organization_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="organization not found"
            )
        return organization
    
    def list_organizations(self,current_user:User):
        """Return the current user's own organization."""
        statement=select(Organization).where(Organization.id==current_user.organization_id)
        result=self.db.execute(statement)
        return result.scalars().all()

    def update_organization(self,organization_id:int,organization_data:OrganizationUpdate,current_user:User):
        """updates the  organization."""
        organization=self.get_organization(organization_id,current_user)
        update_data=organization_data.model_dump(exclude_unset=True)



        for field,value in update_data.items():
            setattr(organization,field,value)


        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Organization slug already exists."
            )

        self.db.refresh(organization)
        return organization

    def delete_organization(self,organization_id:int,current_user:User):
        """Delete an organization by its ID."""
        organization=self.get_organization(organization_id,current_user)
        self.db.delete(organization)
        self.db.commit()


    


    