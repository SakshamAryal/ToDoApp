from fastapi import FastAPI
from todo.api.routes.users import user_route

app = FastAPI()


@app.get("/")
def check_app():
    pass
