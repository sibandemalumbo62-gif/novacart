from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from backend.database import SessionLocal, engine
from backend import models, schemas, auth

# ---------------- APP INIT ----------------
app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- DB SESSION ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- CREATE TABLES (FIXED) ----------------
@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)

# ---------------- AUTH SETUP ----------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ---------------- REGISTER ----------------
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = auth.hash_password(user.password)

    new_user = models.User(
        username=user.username,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

# ---------------- LOGIN ----------------
@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(models.User).filter(
        models.User.username == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not auth.verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = auth.create_access_token({"sub": db_user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# ---------------- CREATE PRODUCT ----------------
@app.post("/products")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):

    new_product = models.Product(
        name=product.name,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

# ---------------- GET PRODUCTS ----------------
@app.get("/products")
def get_products(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return db.query(models.Product).all()

# ---------------- UPDATE PRODUCT ----------------
@app.put("/products/{id}")
def update_product(
    id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):

    db_product = db.query(models.Product).filter(
        models.Product.id == id
    ).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.name = product.name
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)

    return db_product

# ---------------- DELETE PRODUCT ----------------
@app.delete("/products/{id}")
def delete_product(
    id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):

    db_product = db.query(models.Product).filter(
        models.Product.id == id
    ).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()

    return {"message": "Product deleted successfully"}