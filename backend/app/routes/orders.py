from fastapi import APIRouter, HTTPException
from app.database.simple_db import cursor, conn
from datetime import datetime

router = APIRouter()


@router.post("/orders")
def create_order(supplier_id: int, product: str, quantity: int, price: float):

    #проверяем suppliers
    cursor.execute("SELECT * FROM suppliers WHERE id = ?", (supplier_id,))
    supplier = cursor.fetchone

    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    if not quantity <= 0:
        raise HTTPException(status_code=400, detail="Quatity must be > 0")
    
    if not price <= 0:
        raise HTTPException(status_code=400, detail="Price must be > 0")
    
    total = quantity * price
    create_at = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO oders (supplier_id, product, quantity, price, total, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (supplier_id, product, quantity, price, total, create_at))

    conn.commit()

    return {
        "supplier_id": supplier_id,
        "product": product,
        "quatity": quantity,
        "price": price,
        "total": total
    }

@router.get("/orders")
def list_orders():

    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "supplier_id": row[1],
            "product": row[2],
            "quantity": row[3],
            "price": row[4],
            "total": row[5],
            "created_at": row[6]
    })
    
    return result