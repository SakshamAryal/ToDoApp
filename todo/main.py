from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def check_app():
    return "hello world"