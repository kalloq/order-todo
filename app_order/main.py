from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

class Order(BaseModel):
    email: str
    shipping_address: str
    product_id: int

products = [
    Product(id=1, name="Laptop", price=1000.0),
    Product(id=2, name="Smartphone", price=500.0),
    Product(id=3, name="Headphones", price=150.0),
]

orders = []

@app.get("/products", response_model=List[Product])
def get_products():
    return products

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    product_exists = any(product.id == order.product_id for product in products)
    if not product_exists:
        raise HTTPException(status_code=400, detail="Invalid product ID")

    orders.append(order)
    return order

@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders
