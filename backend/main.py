from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.database import Base, engine, SessionLocal
from backend.schemas import ProductCreate, ProductResponse
from backend.services import product_service

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/products", response_model=ProductResponse)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product.name, product.price)


@app.get("/products", response_model=list[ProductResponse])
def get_all(db: Session = Depends(get_db)):
    return product_service.get_products(db)


@app.get("/products/{product_id}", response_model=ProductResponse)
def get_one(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product(db, product_id)


@app.delete("/products/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)