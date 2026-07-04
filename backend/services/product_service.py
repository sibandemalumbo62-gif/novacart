from sqlalchemy.orm import Session
from backend.repositories import product_repo


def create_product(db: Session, name: str, price: int):
    return product_repo.create_product(db, name, price)


def get_products(db: Session):
    return product_repo.get_products(db)


def get_product(db: Session, product_id: int):
    return product_repo.get_product(db, product_id)


def delete_product(db: Session, product_id: int):
    return product_repo.delete_product(db, product_id)