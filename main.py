from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

from src.lib.managedb import ManageDB

class Product(BaseModel):
    id : str = str(uuid4()) 
    name: str 
    amount: int
    price: float
   

app:FastAPI = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"} 

@app.get("/api/products")
def get_products():
    return ManageDB().read_products()

@app.get("/api/products/{product_id}")
def get_single_products(product_id: str):
    products: list = ManageDB().read_products()
    for product in products:
        if str(product["id"]) == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/api/products")
def create_product(product: Product):
    products: list = ManageDB().read_products()
    products.append(product.dict())
    ManageDB().write_products(products)
    return {"Success":True,
            "Message":"Product added successfully",
            "Value":product.dict()
            }

@app.put("/api/products/{product_id}")
def update_product(product_id: str, product: Product):
    products: list = ManageDB().read_products()
    for index, prod in enumerate(products):
        if prod["id"] == product_id:
            products[index] = product.dict()
            ManageDB().write_products(products)
            return {"Success":True,
                    "Message":"Product updated successfully",
                    "Value":product.dict()
                    }
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/api/products/{product_id}")
def delete_product(product_id: str):
    products: list = ManageDB().read_products()
    for index, prod in enumerate(products):
        if prod["id"] == product_id:
            products.pop(index)
            ManageDB().write_products(products)
            return {"Success":True,
                    "Message":"Product deleted successfully",
                    "Value":product_id
                    }
    raise HTTPException(status_code=404, detail="Product not found")