from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette import status
from starlette.exceptions import HTTPException
from todo.api.auth_utils import verify_password
from todo.config import settings
from todo.jwt_handler import create_access_token, create_refresh_token, decode_token
from todo.models.user import User
from todo.schemas.token import Token
from todo.dependencies.db_dependency import get_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", response_model= Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Any:
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject= user.email,
        expires_delta=access_token_expires,
    )
    new_refresh_token = create_refresh_token(
        subject= user.email )
    return {
        "access_token": access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer",
    }

@router.post("/refresh", response_model= Token)
async def refresh_token(refresh_token: str= Body(...), db: Session = Depends(get_db)) -> Any:
    try:
        payload = decode_token(refresh_token)
        if "token_type" not in payload or payload["token_type"] != "refresh":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid refresh token",
            )
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
            )
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            subject=email,
            expires_delta=access_token_expires
        )
        new_refresh_token = create_refresh_token(subject=email)
        return {
            "access_token": access_token,
            "refresh_token": new_refresh_token,
            "token_type": "bearer",
        }
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            )
