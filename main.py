from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from schemas import UserCreate
from crud import create_user, get_user_by_email

# Initialize the app and create tables
app = FastAPI()
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=dict)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered")

    new_user = create_user(db, user.email, user.password, user.age)
    return {"message": "User registered successfully", "user": {"id": new_user.id, "email": new_user.email, "age": new_user.age}}
