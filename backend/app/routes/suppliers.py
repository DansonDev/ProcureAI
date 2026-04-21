from fastapi import APIRouter, HTTPException
from app.database.simple_db import cursor, conn


router = APIRouter()


@router.get("/suppliers")
def list_suppliers(limit: int=10): #limit of suppliers at one page
    cursor.execute(
        "SELECT * FROM suppliers LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()

    result = []
    
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "price": row[2]
        })


    return result


@router.post("/suppliers")
def add_supplier(name: str, price: float):
    if price < 0:
        raise HTTPException(status_code=400, detail="Price must be positive")
    
    try:
        cursor.execute(
            "INSERT INTO suppliers (name, price) VALUES (?, ?)",
            (name, float(price))
        )
        conn.commit()

        supplier_id = cursor.lastrowid

        return {
            "id": supplier_id,
            "name": name,
            "price": price
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: int):
    cursor.execute(
        "SELECT * FROM suppliers WHERE id = ?",
        (supplier_id,)
    )
    supplier = cursor.fetchone()

    if not supplier:
        raise HTTPException(status_code=404, detail=f"Supplier {supplier_id} not found")
    
    return {
        "id": supplier[0],
        "name": supplier[1],
        "price": supplier[2],
    }