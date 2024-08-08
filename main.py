from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def display():
    return{"Message":"Hello"}

