import json
import os

def query_inventory(sku: str) -> dict:
    file_path = os.path.join("data", "inventory.json")
    try:
        with open(file_path, "r") as f:
            db = json.load(f)
        return db.get(sku, {"error": f"SKU {sku} not found in master data."})
    except FileNotFoundError:
        return {"error": "Database connection failed."}