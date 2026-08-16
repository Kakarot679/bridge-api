from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jwt import PyJWTError
from app.core.security import decode_access_token
from app.db.session import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credential_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload=decode_access_token(token)
    except PyJWTError:
        raise credential_exception


    user_id=payload.get("sub")
    if user_id is None:
        raise credential_exception

    user=db.get(User,int(user_id))
    if user is None:
        raise credential_exception
    return user