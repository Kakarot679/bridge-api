from fastapi import FastAPI
from app.core.config import settings
from app.routers.provider import router as provider_router
from app.routers.organization import router as organization_router
from app.routers.connection import router as connection_router 
from app.routers.endpoint import router as endpoint_router
from app.routers.auth import router as auth_router
from app.models.organization import Organization
from app.models.user import User
from app.models.provider import Provider
from app.models.connection import Connection
from app.models.endpoint import Endpoint

app=FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG)
app.include_router(provider_router)
app.include_router(connection_router)
app.include_router(endpoint_router)
app.include_router(auth_router)

app.include_router(organization_router)
@app.get("/")
def run():
    return {
       "title":settings.APP_NAME,
       "version":settings.APP_VERSION,
         "debug":settings.DEBUG
    }
