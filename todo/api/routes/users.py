from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from todo.models.user import User
from todo.schemas.user import UserCreate, UserResponse
from todo.dependencies.db_dependency import get_db
from todo.api.auth_utils import get_hashed_password, verify_password
from todo.dependencies.user_dependency import get_current_user


user_route = APIRouter(
    prefix="/users",
    tags=["users"],
)

@user_route.post("/create_user")
def create_user(create_user_request: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        email=create_user_request.email,
        username=create_user_request.username,
        hashed_password=get_hashed_password(create_user_request.password),
    )
    db.add(new_user)
    db.commit()

@user_route.get("/me", response_model=UserResponse)
async def get_current_user(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user:
        raise HTTPException(status_code=401, detail="Please Login.")
    return user
