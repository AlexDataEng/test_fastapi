from fastapi import FastAPI
import model
from config import engine
import router

app = FastAPI()

@app.get("/")
def home():
    return "Hola"

app.include_router(router, prefix="/book", tags=["book"])

# uvicorn main:app --reload