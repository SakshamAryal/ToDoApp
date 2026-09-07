from fastapi import FastAPI
from todo.api.routes.todo import todo
from todo.api.routes.auth import auth
from todo.api.routes.users import user_route
from todo.api.routes.admin import admin


app = FastAPI()

app.include_router(todo)
app.include_router(auth)
app.include_router(user_route)
app.include_router(admin)

@app.get("/")
def check_app():
    return {"message": "App is running."}
