import sqlite3

conn = sqlite3.connect("procurex_ai.db", check_same_thread=False)
cursor = conn.cursor()

# suppliers
cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
)
""")

# orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER,
    product TEXT,
    quantity INTEGER,
    price REAL,
    total REAL,
    created_at TEXT
)
""")

conn.commit()