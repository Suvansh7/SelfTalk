from fastapi import FastAPI
import llm
app = FastAPI()

@app.get("/get")
def display(name: str):
    return{"Message":f"Hello {llm.testing()}"}

if __name__ == "__main__":
    app()