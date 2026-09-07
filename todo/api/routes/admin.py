from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from todo.dependencies.db_dependency import get_db
from todo.dependencies.user_dependency import get_current_user
from todo.schemas.user import UserResponse
from todo.schemas.task import TaskResponse
from todo.models.user import User
from todo.models.task import Task


admin = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

@admin.delete("/task/{task_id}")
async def admin_delete_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user or not user.admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}


@admin.delete("/user/{user_id}")
async def admin_delete_user(user_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user or not user.admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    target_user = db.query(User).filter(User.id == user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(target_user)
    db.commit()
    return {"message": "User deleted successfully"}


@admin.get("/all-tasks", response_model=list[TaskResponse])
async def admin_get_all_tasks(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user or not user.admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    tasks = db.query(Task).all()
    return tasks


@admin.get("/all-users", response_model=list[UserResponse])
async def admin_get_all_users(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user or not user.admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    users = db.query(User).all()
    return users