from fastapi import FastAPI

app = FastAPI()  # This is the variable Uvicorn looks for

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello, world!"}
