from fastapi import APIRouter, HTTPException

router = APIRouter()

suppliers = []
current_id = 1


@router.get("/suppliers")
def list_suppliers(limit: int=10): #limit of suppliers at one page, changing by user_resolution
    return suppliers[:limit]


@router.post("/suppliers")
def add_supplier(name: str, price: float):
    global current_id

    if price < 0:
        raise HTTPException(status_code=400, detail="Price must be positive")

    supplier = {
        "id": current_id,
        "name": name,
        "price": price
    }

    suppliers.append(supplier)
    current_id += 1

    return supplier


@router.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: int):
    for supplier in suppliers:
        if supplier["id"] == supplier_id:
            return supplier

    raise HTTPException(status_code=404, detail=f"Supplier {supplier_id} not found")