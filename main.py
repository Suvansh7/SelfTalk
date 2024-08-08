from fastapi import FastAPI
import llm
app = FastAPI()

@app.get("/")
def display():
    return{"Message":f"Hello {llm.testing()}"}

