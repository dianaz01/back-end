from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserLogin
from database import SessionLocal
from auth_utils import hash_password, verify_password

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def register_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_pw = hash_password(user.password)
    new_user = User(username=user.username, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created", "username": new_user.username}

def login_user(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"msg": "Login successful", "username": db_user.username}