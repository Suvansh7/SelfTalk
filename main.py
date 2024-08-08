from fastapi import FastAPI
from typing import Uvicorn
import llm
app = FastAPI()

@app.get("/")
def display():
    return{"Message":"Hello"}

