from fastapi import APIRouter,Form
import secrets


router=APIRouter(prefix="/fake-provider",tags=["Fake Provider(testing only)"])

@router.post("/oauth/token")
def fake_token_endpoint(grant_type:str=Form(...),refresh_token:str=Form(...)):
    new_access_token="fake_"+secrets.token_hex(16)
    return{
        "access_token":new_access_token,
        "expires_in":3600
    }