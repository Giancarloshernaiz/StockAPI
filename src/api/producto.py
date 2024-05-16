from fastapi import APIRouter, HTTPException
from src.lib.managedb import ManageDB
from pydantic import BaseModel
from uuid import uuid4

router_productos = APIRouter()
manage = ManageDB()

class Product(BaseModel):
    id : str = str(uuid4()) 
    name: str 
    amount: int
    price: float


@router_productos.get("/")
def root():
    return {"Hello": "World"} 

@router_productos.get("/products")
def get_products():
    return manage.read_products()

@router_productos.get("/products/{product_id}")
def get_single_products(product_id: str):
    products: list = manage.read_products()
    for product in products:
        if str(product["id"]) == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router_productos.post("/products")
def create_product(product: Product):
    products: list = manage.read_products()
    products.append(product.dict())
    manage.write_products(products)
    return {"Success":True,
            "Message":"Product added successfully",
            "Value":product.dict()
            }

@router_productos.put("/products/{product_id}")
def update_product(product_id: str, product: Product):
    products: list = manage.read_products()
    for index, prod in enumerate(products):
        if prod["id"] == product_id:
            products[index] = product.dict()
            manage.write_products(products)
            return {"Success":True,
                    "Message":"Product updated successfully",
                    "Value":product.dict()
                    }
    raise HTTPException(status_code=404, detail="Product not found")

@router_productos.delete("/products/{product_id}")
def delete_product(product_id: str):
    products: list = manage.read_products()
    for index, prod in enumerate(products):
        if prod["id"] == product_id:
            products.pop(index)
            manage.write_products(products)
            return {"Success":True,
                    "Message":"Product deleted successfully",
                    "Value":product_id
                    }
    raise HTTPException(status_code=404, detail="Product not found")