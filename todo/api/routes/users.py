from fastapi import APIRouter

from todo.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/create", response_model=User)
async def create_user(user: User):



