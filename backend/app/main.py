from fastapi import FastAPI, HTTPException
from app.routes import suppliers, orders

app = FastAPI()

app.include_router(suppliers.router)
app.include_router(orders.router)


@app.get("/")
def root():
    return {"message": "ProcurexAI is working"}
