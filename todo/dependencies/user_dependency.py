from datetime import datetime, timezone

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from pydantic import ValidationError

from todo.jwt_handler import decode_token
from todo.schemas.token import TokenPayload
from fastapi import Depends, HTTPException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token:str = Depends(oauth2_scheme)) -> str:
    try:
        payload = decode_token(token)
        token_data = TokenPayload(**payload)
        if token_data.exp is None:
            raise HTTPException(status_code=401, detail="Token missing expiration")
        if token_data.sub is None:
            raise HTTPException(status_code=404, detail="Token missing sub")
        if datetime.fromtimestamp(token_data.exp, tz=timezone.utc) < datetime.now(timezone.utc):
            raise HTTPException(status_code=403, detail="Token expired")
        return token_data.sub
    except (JWTError, ValidationError) :
        raise HTTPException(status_code=403, detail="Could not validate credentials")
