from datetime import datetime
from pydantic import BaseModel, Field, FutureDatetime, ConfigDict
from typing import Annotated

class TaskCreate(BaseModel):
    title: Annotated[str, Field(min_length=3)]
    description: Annotated[str, Field(min_length=1, max_length=180)]
    completed: bool = Field(default=False)
    priority: Annotated[int, Field(gt=0, lt=6)]
    deadline: FutureDatetime | None = None


class TaskUpdate(BaseModel):
    description: Annotated[str, Field(min_length=1, max_length=180)]
    completed: bool = Field(default=False)
    priority: int
    deadline: datetime


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: int
    deadline: datetime | None = None
    completed: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
