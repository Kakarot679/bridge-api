from fastapi import FastAPI
from app.core.config import settings

app=FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG)

@app.get("/")
def run():
    return {
       "title":settings.APP_NAME,
       "version":settings.APP_VERSION,
         "debug":settings.DEBUG
    }