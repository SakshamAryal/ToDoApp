from datetime import datetime, timezone
from todo.models.user import User
from todo.models.task import Task
from todo.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from todo.dependencies.user_dependency import get_current_user
from todo.dependencies.db_dependency import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

todo = APIRouter(
    prefix="/todo",
    tags= ["todo"]
)

@todo.post("/create")
async def create_task(new_task: TaskCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user:
        raise HTTPException(status_code=401, detail="Not Authorized.")
    db_task = Task(**new_task.model_dump())
    db_task.author = user.username
    db_task.created_at = datetime.now(timezone.utc)
    db_task.updated_at = db_task.created_at
    db.add(db_task)
    db.commit()

@todo.get("/task/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task or db_task.author != user.username:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@todo.get("/task", response_model=TaskResponse)
async def get_all_tasks(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == current_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    tasks = db.query(Task).filter(Task.author == user.username).all()
    return tasks
