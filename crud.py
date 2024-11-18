from sqlalchemy.orm import Session
from models import User
from utils import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, password: str, age: int):
    new_user = User(email=email, hashed_password=hash_password(password), age=age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user