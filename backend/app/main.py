from fastapi import FastAPI, HTTPException
from app.routes import suppliers

app = FastAPI()

app.include_router(suppliers.router)


@app.get("/")
def root():
    return {"message": "ProcurexAI is working"}
