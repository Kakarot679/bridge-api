from fastapi import FastAPI
from app.core.config import settings
from app.routers.provider import router as provider_router
from app.models.organization import Organization
from app.models.user import User
from app.models.provider import Provider
from app.models.connection import Connection
from app.models.endpoint import Endpoint

app=FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG)
app.include_router(provider_router)
@app.get("/")
def run():
    return {
       "title":settings.APP_NAME,
       "version":settings.APP_VERSION,
         "debug":settings.DEBUG
    }
